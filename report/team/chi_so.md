# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

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
- **Chỉ số Dùng & An toàn tự đề xuất (chờ TV3 chốt tên cuối ở bảng E1):**
  - Nếu dùng *% yêu cầu nhóm can thiệp có mở trợ lý*: đo được từ `agent_suggestion_shown` ÷ `refund_request_created` (`arm == 'treatment'`).
  - Nếu dùng *% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần*: đo được từ `audit_sample_checked` (`chenh_lech != 0`).
  - Nếu TV3 đề xuất chỉ số khác ngoài 10 event trên, cần bổ sung event có `trace_id` tương ứng hoặc ghi rõ *chưa đo được* trước khi chốt CP5.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
