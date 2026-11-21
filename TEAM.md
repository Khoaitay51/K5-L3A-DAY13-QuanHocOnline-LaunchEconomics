# Team

## Thông tin nhóm

- Tên nhóm: `QuanHocOnline`
- Lớp: `L3A`
- Repo nhóm: `K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/Khoaitay51/K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` · nhánh `main` · commit chốt nội dung `867534a` (commit ngay sau chỉ ghi dòng này)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Trường Chinh | 2A202603426 | phemchinh1708@gmail.com | Khoaitay51 | Người viết code (CP1–CP2) → Kỹ sư kiểm chứng & Event (CP3–CP5) |
|   2 | Nguyễn Minh Quân | 2A202603510 | minhquan2955@gmail.com | minhquan2955 | Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5) |
|   3 | Trần Quang Nam | 2A202603516 | wgnam2k4@gmail.com | wgnam2k4 | Người gắn nhãn 1 & QA / Gatekeeper |
|   4 | Nguyễn Văn Ba | 2A202603489 | nguyenvanba.tinhoc@gmail.com | xtraiter | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Phần việc, đóng góp và bằng chứng của từng thành viên:

## PhamTruongChinh-2A202603426

### Phần việc phụ trách

- Cài đặt môi trường Python (`.venv`), lập trình `src/lab13.py` cho CP1 (A1–A4) và CP2 (B1–B4), bàn giao code cho TV2 sau giờ giải lao.
- Thiết kế danh sách 10 event có `trace_id` và ánh xạ kiểm tra chéo trong `report/team/chi_so.md`.
- Lập kế hoạch phân việc & timeline 4 người (`IMPLEMENTATION_PLAN.md`), thực hiện kiểm tra kỹ thuật YAML/checklist cuối buổi.

### Đóng góp cụ thể

- Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Viết `mo_hinh(...)` và các bảng tính A2–A4, độ nhạy B1–B4 trên dữ liệu giả lập (gắn nhãn `simulated` đầy đủ).
- Hoàn thiện phần Danh sách event (10 event có `trace_id`) và Kiểm tra chéo event ↔ chỉ số trong `report/team/chi_so.md`.

### Bằng chứng

- `src/lab13.py`, `report/team/chi_so.md` (phần Danh sách event & Kiểm tra chéo), `report/team/2A202603426_PhamTruongChinh.md`, `IMPLEMENTATION_PLAN.md`.

## NguyenMinhQuan-2A202603510

### Phần việc phụ trách

- Kiểm số và điền bảng chi phí A1–A4, B1–B4.
- Tiếp quản `src/lab13.py` để tính cỡ mẫu pilot D1 và ba chỉ số E1. Ghi số liệu D1 trong kế hoạch pilot và lập bảng rủi ro kinh tế E2.

### Đóng góp cụ thể

- Đối chiếu chi phí theo giới hạn số lần chạy. Hai lần chạy cho chi phí toàn hệ thống thấp nhất là 6.901.220 đ (`simulated`).
- Tính phương án 20 nhân viên mỗi nhóm, tối thiểu 299 yêu cầu mỗi người để phát hiện chênh lệch 6 điểm phần trăm, và power 64,17% nếu tác động thật chỉ đạt 5 điểm.
- Tính các tỷ lệ quan sát E1 là 82,83%, 27,12% và 4,25%. Ghi ba rủi ro kinh tế về làm lại, xem lại và khối lượng.

### Bằng chứng

- `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` (D1), `report/team/chi_so.md` (số E1 và bảng E2), `report/team/2A202603510_NguyenMinhQuan.md`.

## TranQuangNam-2A202603516

### Phần việc phụ trách

- Đảm nhiệm vai trò Người gắn nhãn 1 & QA / Gatekeeper, giám sát chất lượng hồ sơ và bám sát Rubric C1–C8.
- Gắn nhãn độc lập 20 ca lỗi CP3 theo 5 nhóm Google PAIR, tính đồng thuận (đạt 90,0%) và chủ trì hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Hoàn thiện 5 câu D2 "tách được tác động", đánh đổi MDE 6 điểm và power 64,17%, tỉ lệ mở lại hiện tại (3,97%–4,25%) và 3 luật dừng định lượng 4 vế trong `report/team/pilot_plan.yaml`.
- Đề xuất 2 chỉ số mới (Dùng & An toàn) trong `report/team/chi_so.md`; phối hợp rà soát và khóa hồ sơ 1 trang `report/team/ho_so_launch_v0.md`.
- Đại diện nhóm chủ trì chấm phản biện chéo nhóm **PhanDao** tại `report/team/phieu_cham.md` (30/30đ, Go có điều kiện) và viết báo cáo nhóm `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, trùng 18/20 ca với TV4 (90,0% đồng thuận); chốt nhãn thống nhất khớp 20/20 với chuẩn Google PAIR; lập bảng 5 ca khắc phục đo được có ngưỡng và vai trò phụ trách.
- Xây dựng 3 luật dừng 4 vế (An toàn, Chi phí, Mức độ sử dụng) và quy trình rollback 30 phút trong `pilot_plan.yaml`; làm sạch mọi dấu `?` và verify với `yaml.safe_load`.
- Đề xuất 2 chỉ số đo lường trong pilot: % mở gợi ý trợ lý nhóm can thiệp và % đơn hoàn sai tiền qua kiểm toán mẫu hằng tuần để bắt lỗi ngầm.
- Hoàn thiện và khóa hồ sơ launch v0 đúng 1 trang, đủ 7 mục có số định lượng, trạng thái hợp lệ và đề xuất Go có điều kiện có 4 điều kiện, mỗi điều kiện một vai trò và ngày kiểm tra.
- Chấm chéo nhóm PhanDao 30/30 điểm trên `phieu_cham.md`, đặt câu hỏi về chi phí cố định ở bước rollout 0.10 (≈ 15.266 đ = 1,27× [simulated]), và viết báo cáo nhóm 8 mục chuẩn `group_report.md`.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `report/team/2A202603516_TranQuangNam.md`.

## NguyenVanBa-2A202603489

### Phần việc phụ trách

- Người gắn nhãn 2 (CP3) kiêm người giữ hồ sơ `report/team/ho_so_launch_v0.md`.
- Tích hợp nhánh của các thành viên vào `main` và rà soát toàn bộ hồ sơ trước khi nộp.

### Đóng góp cụ thể

- Merge nhánh `tranquangnam` vào `main` (không xung đột); chạy lại toàn bộ checklist nộp bài (`lab13.py`, `yaml.safe_load`, dấu `?`, từ cấm).
- Sửa `src/lab13.py` để `python lab13.py` chạy được trên console Windows (trước đó lỗi `UnicodeEncodeError` ngay dòng đầu).
- Sửa `ho_so_launch_v0.md`: tách điều kiện có hai vai phụ trách thành hai điều kiện một vai; thêm điều kiện ký chấp nhận MDE 6 điểm (power 64,17%).
- Bổ sung lý do loại `doi_tac` (0,85×, `simulated`) ở A3; sửa câu sai về kết quả duyệt chéo trong `group_report.md`.
- Gate 2a: gửi hồ sơ cho hội đồng PhanDao, trình bày và trả lời câu hỏi về mốc ký chấp nhận MDE 6 điểm; nhóm được chấm 30/30, quyết định Go có điều kiện. Sửa theo góp ý: dời điều kiện 4 từ 2026-12-15 về 2026-12-05, trước khi mở pilot.
- Ghi kết quả duyệt chéo vào `group_report.md`, hoàn thiện `phieu_cham.md` (nhóm chấm PhanDao) cùng TV3, chốt `TEAM.md` và commit nộp bài.

### Bằng chứng

- Commit `50a4b33` (merge nhánh TV3), `5ca07d8` (sửa lỗi Windows và hồ sơ), `ea37570` (kết quả Gate 2a, dời điều kiện 4), `74cd5f4` (phiếu chấm PhanDao); `report/team/2A202603489_NguyenVanBa.md`.

