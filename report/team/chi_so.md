# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = **4,25%** |
| Dùng | Nhóm tự đề xuất: Tỉ lệ mở gợi ý trợ lý trong nhóm can thiệp | Số yêu cầu có nhân viên bấm xem gợi ý của trợ lý, chia tổng số yêu cầu nhóm can thiệp tiếp nhận | Đề xuất đo trong pilot (qua `agent_suggestion_shown` ÷ `refund_request_created`) |
| An toàn | Nhóm tự đề xuất: Tỉ lệ sai sót số tiền hoàn qua kiểm toán mẫu | Số đơn có chênh lệch tiền hoàn (`chenh_lech != 0`), chia tổng số đơn kiểm toán mẫu ngẫu nhiên hằng tuần | Đề xuất đo trong pilot (qua `audit_sample_checked` để bắt lỗi ngầm) |

Đây là các chỉ số quan sát trong đợt chạy thử trên bộ dữ liệu giả lập. Pilot có đối chứng song song sẽ dùng để ước lượng tác động của trợ lý.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, loai, so_tien_vnd, depot, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí | `run_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id, request_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai_thuc, trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id, phut_lam_lai_thuc, ly_do, trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien_vnd, ket_qua_ghi_so, trace_id` | Khi hệ thống ghi giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí | `reason, tom_tat, loai, trace_id` | Khi chuyển yêu cầu sang nhân viên tự xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id, closed_at, ket_qua, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | App khách / CSKH | `request_id, reopened_at, reason, trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán | `request_id, so_tien_da_hoan, so_tien_dung, chenh_lech, trace_id` | Khi kiểm toán mẫu hằng tuần để phát hiện lỗi ngầm |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24 giờ và không mở lại trong 7 ngày):** Tính từ `refund_request_created` + `ticket_closed` (`closed_at - created_at <= 24h`) + kiểm tra không phát sinh `ticket_reopened` trong 7 ngày cùng `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Tính từ `staff_review_decision` (đếm `quyet_dinh` là `sua` hoặc `bo` chia cho tổng số lượt có `staff_review_decision`) nối qua `trace_id`.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Tính từ `ticket_reopened` (trong 7 ngày) chia cho tổng số `refund_request_created` cùng `trace_id`.
- **Chi phí thật thay thế số `simulated` ở tuần 1 pilot:** Tính từ `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`), `staff_review_decision` (`phut_xem_lai_thuc`), `staff_rework_completed` (`phut_lam_lai_thuc`) và `ticket_closed`.
- **Chỉ số Dùng đề xuất (% mở gợi ý trợ lý nhóm can thiệp):** Đo được bằng cách đếm số `refund_request_created` (`arm == 'treatment'`) có phát sinh ít nhất một event `agent_suggestion_shown` cùng `trace_id`.
- **Chỉ số An toàn đề xuất (% đơn hoàn sai tiền qua kiểm toán mẫu):** Đo được bằng cách đếm số event `audit_sample_checked` có `chenh_lech != 0` chia cho tổng số event `audit_sample_checked` ghi nhận trong đợt kiểm toán tuần.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Nếu số ca làm lại gấp đôi, chi phí tăng từ 4.472 lên **6.787 đ/việc thành công (+51,8%)** (`simulated`, B1). | Theo dõi số ca và tổng phút qua `staff_rework_completed` hằng tuần, phân theo loại yêu cầu. | Rà nguyên nhân của loại tăng mạnh nhất và tạm chuyển các ca thuộc loại đó sang xử lý thủ công trong khi khắc phục. | Trưởng nhóm CSKH |
| Duy trì xem lại 100% gợi ý | Tốn **11.743 đ (0,98×)** với 9 phút làm lại, hoặc **12.415 đ (1,03×)** với trung bình từ CSV xấp xỉ 15,30 phút (`simulated`, B4). | Theo dõi tỉ lệ gợi ý được xem lại và phút xem lại mỗi ca qua `agent_suggestion_shown` và `staff_review_decision`. | Rà chi phí theo tuần, giữ phạm vi hiện tại khi vượt ngưỡng hòa vốn 4,8 phút/ca trong kịch bản làm lại dài hơn (`simulated`). | Quản lý sản phẩm |
| Khối lượng giảm một nửa | Phần cố định tăng từ 1.185 lên **2.370 đ/việc thành công**, đưa chi phí lên **5.784 đ/việc thành công** (`simulated`, A4). | Theo dõi khối lượng và số việc thành công hằng tuần từ `refund_request_created` và `ticket_closed` trong phạm vi pilot. | Tính lại chi phí theo khối lượng quan sát được trước khi quyết định mở rộng. | Giám đốc vận hành |
