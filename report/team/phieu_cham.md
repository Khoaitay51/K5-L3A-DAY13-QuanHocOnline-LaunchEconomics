# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): `QuanHocOnline` (Lớp `L3A`)
- Nhóm được chấm: `Nhóm 2` (Lớp `L3A`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Nhóm nêu rõ các con số bất lợi: power chỉ đạt 64,17% nếu tác động thật là 5 điểm ở n=859; kịch bản xem lại 100% với phút làm lại thực tế 15,30 phút có chi phí 12.415 đ (1,03× so với 12.000 đ tự làm, `simulated`); tỉ lệ mở lại nền đã là 3,97%–4,25%. Đề xuất Go có điều kiện có người phụ trách và ngày kiểm tra cụ thể. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn nhãn `simulated` đầy đủ trên toàn bộ các con số phát sinh từ phút xem lại/làm lại giả lập (4.472 đ, 2.696 đ, 8.221 đ, 4.599 đ, bảng B1–B4). Phạm vi pilot thu hẹp rõ ràng vào `noi_dia` (0,22×) và `hang_nang` (0,69×); loại `quoc_te` (1,88×, thành công chỉ 27,3%) và `doi_tac` (0,85×) kèm phân tích định lượng thuyết phục. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Thiết kế đối chứng song song 20 nhân viên can thiệp vs 20 nhân viên chứng làm cùng thời gian, cùng 12 depot; đạt n_hiệu_dụng = 859 (m ≥ 299 yc/nhân viên, DE = 6,96); 3 luật dừng định lượng đủ 4 vế (NẾU – TRONG – THÌ – KHÔNG THÌ) có ngưỡng mở lại ≥ 2 điểm hoặc vượt 6%, chi phí > 8.000 đ, bỏ qua > 40%, có người có quyền dừng (Giám đốc vận hành) trong 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ chặt chẽ về mặt kinh tế học và phương pháp luận thống kê; tính toán chi phí trung thực khi cộng chi phí nhân viên xử lý ca lỗi (5.865 đ/yêu cầu = 0,49×); công khai đánh đổi cỡ mẫu khi power giảm còn 64,17% và rủi ro xem lại 100% có thể đắt hơn tự làm (1,03×).

**Một câu hỏi cho đội trình:** Nếu trong tuần đầu chạy thử nghiệm pilot, nhóm nhận thấy tỉ lệ xem lại của nhân viên lên tới 100% và thời gian làm lại trung bình là 15,3 phút khiến chi phí đội lên 12.415 đ (1,03× so với nhân viên tự làm), nhóm sẽ kích hoạt biện pháp kỹ thuật hoặc quy trình nào để tránh thua lỗ?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội trình giải thích rằng nhóm đã tính toán ngưỡng xem lại hòa vốn tối đa là 4,8 phút/ca. Nếu tuần đầu tỉ lệ xem lại chạm 100%, Trưởng nhóm CSKH sẽ ngay lập tức kích hoạt chính sách kiểm tra mẫu 20% đối với các yêu cầu có độ tin cậy cao trên trace, đồng thời đặt trần thời gian xem lại cho nhân viên tối đa 3 phút/ca. Nếu sau 2 tuần chi phí mỗi việc thành công vẫn duy trì trên 8.000 đ, luật dừng số 2 sẽ được kích hoạt để lập tức thu hẹp phạm vi chỉ còn `noi_dia` (CPS 2.696 đ = 0,22×) và áp trần tối đa 2 lần chạy, bảo toàn hiệu quả kinh tế cho công ty.
