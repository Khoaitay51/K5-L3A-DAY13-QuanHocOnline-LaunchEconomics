"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
KHOI_LUONG_THANG = 45_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=hoa_don_moi_yc,
    )


def in_bang_a2(runs, reqs):
    """In bảng A2 và đối chiếu chi phí cả hệ thống so với baseline 12.000 đ."""
    kq = mo_hinh(runs, reqs)
    so_tool = int(runs['tool_calls'].sum())
    phut_xem_lai = int(reqs['phut_xem_lai_simulated'].sum())
    phut_lam_lai = int(reqs['phut_lam_lai_simulated'].sum())
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    print(f"{'Token (mọi lần chạy)':38s} {kq['token']:>12,.0f} đ  [đo từ trace]")
    print(f"{f'Tool ({so_tool:,} lần gọi)':38s} {kq['tool']:>12,.0f} đ  [đo từ trace]")
    print(f"{'  Trong đó, lần chạy thứ 2 và 3':38s} {kq['chay_lai']:>12,.0f} đ  [đo từ trace]")
    print(f"{f'Xem lại ({phut_xem_lai:,} phút)':38s} {kq['xem_lai']:>12,.0f} đ  [simulated · {kq['xem_lai'] / kq['tong'] * 100:.1f}%]")
    print(f"{f'Làm lại ({phut_lam_lai:,} phút)':38s} {kq['lam_lai']:>12,.0f} đ  [simulated · {kq['lam_lai'] / kq['tong'] * 100:.1f}%]")
    print(f"{'Tổng chi phí':38s} {kq['tong']:>12,.0f} đ  [có phần simulated]")
    print(f"{'Số việc thành công':38s} {kq['thanh_cong']:>12,d} việc")
    print(f"{'Chi phí mỗi việc thành công (CPS)':38s} {kq['cps']:>12,.0f} đ  [simulated]")
    print(f"{'Hoá đơn token + tool / số yêu cầu':38s} {kq['hoa_don_moi_yc']:>12,.1f} đ  [đo từ trace]")
    print(f"Tỉ lệ CPS / hoá đơn mỗi yêu cầu: {kq['cps'] / kq['hoa_don_moi_yc']:.1f}x")
    print(f"Chi phí cả hệ thống/yêu cầu (cộng {khong_tc} ca chuyển/làm lại * 12.000 đ): "
          f"{he_thong_moi_yc:,.0f} đ = {he_thong_moi_yc / BASELINE:.2f}x của 12.000 đ [simulated]")
    return kq


def in_bang_a3(runs, reqs):
    """In bảng A3 theo cột loai và tỉ lệ status == 'ok' theo từng lần thử."""
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'Thành công':>11s} {'Lần chạy/YC':>12s} {'CPS [simulated]':>17s} {'So 12.000đ':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        ti_le_tc = kq['thanh_cong'] / len(sub) * 100
        lan_chay_tb = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>7,d} {ti_le_tc:>10.1f}% {lan_chay_tb:>12.2f} "
              f"{kq['cps']:>15,.0f} đ {kq['cps'] / BASELINE:>10.2f}x")

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['ok'] = (runs_loai['status'] == 'ok').astype(float) * 100
    pivot = runs_loai.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    print('\nTỉ lệ status == ok (%) theo loại và lần thử:')
    print(pivot.round(1).to_string())


def in_bang_a4(runs, reqs):
    """In bảng A4 cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = kq['thanh_cong'] / len(reqs)

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    print(f"CPS biến đổi trong phạm vi: {kq['cps']:,.0f} đ ({kq['thanh_cong']}/{len(reqs)} yc của mẫu) [simulated]")
    for khoi_luong in [KHOI_LUONG_THANG, KHOI_LUONG_THANG // 2]:
        viec_thang = khoi_luong * ti_le_tc_mau
        co_dinh = CHI_PHI_CO_DINH_THANG / viec_thang
        tong_cps = kq['cps'] + co_dinh
        print(f"Khối lượng {khoi_luong:>6,d} yc/tháng -> {viec_thang:>7,.0f} việc TC/tháng | "
              f"Cố định: {co_dinh:>5,.0f} đ | CPS + cố định: {tong_cps:>5,.0f} đ "
              f"({tong_cps / BASELINE:.2f}x) [simulated]")


def in_bang_b1_b2(runs, reqs):
    """In bảng độ nhạy B1 (9 kịch bản), kiểm tra tính tuyến tính và tính cặp B2."""
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    ket_qua_b1 = {}

    print('\n=== B1 · Bảng độ nhạy (CPS [simulated]) ===')
    print(f"{'Kịch bản':28s} {'CPS [sim]':>12s} {'Thay đổi':>10s}")
    print(f"{'Gốc (A2)':28s} {goc:>10,.0f} đ")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        ket_qua_b1[ten] = cps
        print(f"{ten:28s} {cps:>10,.0f} đ {(cps / goc - 1) * 100:>+9.1f}%")

    for tang, giam in [
        ('Giá token gấp đôi', 'Giá token giảm một nửa'),
        ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
        ('Làm lại gấp đôi', 'Làm lại giảm một nửa'),
    ]:
        assert abs((ket_qua_b1[giam] - goc) + 0.5 * (ket_qua_b1[tang] - goc)) < 1e-6

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    print(f"Token gấp đôi + Xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) [simulated]")
    print('Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên')


def in_bang_b3(runs, reqs):
    """In bảng B3 so sánh tổng chi phí trợ lý và chi phí cả hệ thống theo giới hạn lần chạy."""
    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý [sim]':>19s} {'Không TC':>10s} {'Cả hệ thống [sim]':>19s} {'CPS [sim]':>12s}")
    for max_lan in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=max_lan)
        khong_tc = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + khong_tc * BASELINE
        print(f"{f'{max_lan} lần':10s} {kq['tong']:>17,.0f} đ {khong_tc:>10,d} "
              f"{ca_he_thong:>17,.0f} đ {kq['cps']:>10,.0f} đ")


def in_bang_b4(runs, reqs):
    """In kịch bản B4 xem lại 100% cho noi_dia + hang_nang theo cả 9 phút và mức trung bình thực."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]

    so_co_ok = int(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique())
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    so_thanh_cong = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    token_tool = (
        runs_pv['tokens_in'] / 1000 * GIA_VAO
        + runs_pv['tokens_out'] / 1000 * GIA_RA
        + runs_pv['tool_calls'] * GIA_TOOL
    ).sum()
    tien_xem_lai = so_co_ok * 5 * LUONG_PHUT

    lam_lai_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    phut_ll_tb = float(lam_lai_all.mean())

    print('\n=== B4 · Nếu phải xem lại 100% (noi_dia + hang_nang) ===')
    print(f"Số YC phạm vi: {len(pham_vi)} | Có >=1 lần ok: {so_co_ok} | Ca lam_lai: {so_lam_lai} | "
          f"Thành công: {so_thanh_cong} | Token+tool: {token_tool:,.0f} đ")
    print(f"Phút làm lại trên toàn bộ ca lam_lai: trung bình {phut_ll_tb:.2f} phút (trung vị {lam_lai_all.median():.1f} phút)")

    for nhan, phut_ll in [('Giả định 9 phút/ca làm lại', 9.0), (f'Dữ liệu thực {phut_ll_tb:.2f} phút/ca', phut_ll_tb)]:
        tien_lam_lai = so_lam_lai * phut_ll * LUONG_PHUT
        tong = token_tool + tien_xem_lai + tien_lam_lai
        cps = tong / so_thanh_cong
        hoa_von = (so_thanh_cong * BASELINE - token_tool - tien_lam_lai) / (so_co_ok * LUONG_PHUT)
        print(f"- {nhan}: Tổng {tong:,.0f} đ -> CPS {cps:,.0f} đ ({cps / BASELINE:.2f}x) [simulated] | "
              f"Hoà vốn khi xem lại <= {hoa_von:.1f} phút/ca")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_bang_a2(runs, reqs)
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    in_bang_b1_b2(runs, reqs)
    in_bang_b3(runs, reqs)
    in_bang_b4(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
