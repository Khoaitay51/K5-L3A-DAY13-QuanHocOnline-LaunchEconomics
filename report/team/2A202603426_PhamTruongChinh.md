# Báo cáo cá nhân — Phạm Trường Chinh - 2A202603426

## 1. Thông tin thành viên

- Họ tên: Phạm Trường Chinh
- MSSV: `2A202603426`
- Email: `phemchinh1708@gmail.com`
- Vai trong nhóm: **Người viết code (CP1–CP2) → Kỹ sư kiểm chứng & Event (CP3–CP5)**

## 2. Phần việc phụ trách

- **CP0 (Khởi động):** Thiết lập môi trường Python (`.venv` trong `src/`), cài đặt các thư viện trong `src/requirements.txt` (`pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`), cập nhật thông tin nhóm và mục cá nhân trong `TEAM.md`, lập kế hoạch phân việc 4 người tại `IMPLEMENTATION_PLAN.md`.
- **CP1 & CP2 (Code mô hình chi phí và độ nhạy):** Lập trình đầy đủ phần A1, A2, A3, A4 và B1, B2, B3, B4 trong `src/lab13.py`; xuất kết quả để TV2 đối chiếu số và điền `report/team/bang_chi_phi.md`; giữ nguyên phần `# TODO CP4` để bàn giao cho TV2 sau giờ giải lao.
- **CP5 (Event & kiểm tra chéo):** Hoàn thiện mục `## Danh sách event` (10 event có `trace_id`) và `**Kiểm tra chéo:**` trong `report/team/chi_so.md`.
- **Phối hợp còn lại:** Góp ý kỹ thuật cách phát hiện đo được cho bảng 5 ca ở CP3, chạy kiểm chứng `yaml.safe_load` & `grep '?'` cho `pilot_plan.yaml` sau khi TV2/TV3 hoàn thành ở CP4, tham gia duyệt chéo Gate 2a và tự nộp link repo trên LMS trước 23:59 GMT+7.

## 3. Đóng góp cụ thể

- **A1 (Kinh tế chạy lại):** Viết 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; chạy đạt 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`, in `Ba phép thử đáp án biết trước: ĐẠT`).
- **A2 (Mô hình chi phí từ trace):** Viết `mo_hinh(...)` và `in_bang_a2(...)`: Token `245.585 đ` *(đo từ trace)*, Tool `84.000 đ` *(5.600 lần gọi, đo từ trace)*, lần chạy 2 & 3 `93.804 đ` *(đo từ trace)*, Xem lại `1.780.000 đ` *(890 phút, `simulated`, 40,7%)*, Làm lại `2.264.000 đ` *(1.132 phút, `simulated`, 51,8%)*, Tổng `4.373.585 đ` *(có phần `simulated`)*, Số việc thành công `978`, CPS `4.472 đ` `[simulated]` (gấp `16,3×` hoá đơn `274,7 đ`/yêu cầu), chi phí cả hệ thống/yêu cầu `5.865 đ = 0,49×` của `12.000 đ` `[simulated]`.
- **A3 & A4 (Tách theo loại & chi phí cố định):** `noi_dia` `2.696 đ` (`0,22×`), `hang_nang` `8.221 đ` (`0,69×`), `quoc_te` `22.515 đ` (`1,88×`; tỉ lệ `ok` giảm `30,0% → 11,4% → 2,2%` theo lần thử), `doi_tac` `10.215 đ` (`0,85×`) `[simulated]`. Khi cộng cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`: `4.599 đ` (`0,38×`) ở mức 45.000 yc/tháng và `5.784 đ` (`0,48×`) ở mức 22.500 yc/tháng `[simulated]`.
- **B1–B4 (Độ nhạy & xem lại 100%):** Cài đặt 9 kịch bản B1 kèm kiểm tra tuyến tính, B2 (`6.543 đ`, `+46,3%` `[simulated]`; top 3: làm lại `+51,8%`, xem lại `+40,7%`, lương `+23,1%`), B3 (chi phí cả hệ thống thấp nhất ở giới hạn 2 lần: `6.901.220 đ` `[simulated]`, khác với CPS thấp nhất ở 1 lần: `4.111 đ` `[simulated]`), và B4 (`noi_dia` + `hang_nang`: `11.743 đ = 0,98×` với 9 phút làm lại, hoà vốn `<= 5,1 phút/ca`; `12.415 đ = 1,03×` với trung bình thực `15,30 phút/ca`, hoà vốn `<= 4,8 phút/ca` `[simulated]`).
- **Event & Kiểm tra chéo:** Thiết kế 10 event có `trace_id` (`refund_request_created`, `agent_run_completed`, `agent_suggestion_shown`, `staff_review_decision`, `staff_rework_completed`, `refund_ledger_write`, `handoff_to_staff`, `ticket_closed`, `ticket_reopened`, `audit_sample_checked`) và ánh xạ từng chỉ số E1 sang các event tương ứng trong `report/team/chi_so.md`.

## 4. Bằng chứng

- Kế hoạch triển khai nhóm 4 người: `IMPLEMENTATION_PLAN.md` (commit `fbec576`).
- Code chạy từ đầu đến cuối phần A1–A4 và B1–B4: `src/lab13.py`.
- Danh sách 10 event có `trace_id` & bảng kiểm tra chéo: mục `## Danh sách event` và `**Kiểm tra chéo:**` trong `report/team/chi_so.md`.
- Khai báo thành viên và phân công: `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Trợ lý AI lập trình trong IDE (Antigravity) dùng để tóm tắt đề bài, lập `IMPLEMENTATION_PLAN.md`, hỗ trợ viết cấu trúc hàm `src/lab13.py`, đề xuất 10 event trong `report/team/chi_so.md` và rà soát checklist quy định.
- **Cách tự kiểm tra kết quả:**
  1. Tự tạo `.venv` và chạy trực tiếp `cd src && .venv/bin/python lab13.py` trên hai file CSV giả lập gốc (`logix_runs.csv`, `logix_requests.csv`).
  2. Xác nhận 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), kiểm tra tự động tính tuyến tính B1 bằng `assert`, và đối chiếu toàn bộ các con số A2–A4, B1–B4 với ngưỡng sai số `<= 2%` trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
  3. Chạy `grep` kiểm tra không dùng từ cấm theo Quy tắc 5 và không thiếu nhãn `simulated` trên các số tính từ cột `_simulated`.

## 6. Tự đánh giá

- Đã hoàn thành đầy đủ phần việc độc lập của Thành viên 1 đúng phạm vi quyền sở hữu file (Single-Writer), giữ nguyên các file dữ liệu gốc và không làm thay phần việc của TV2, TV3, TV4; mã nguồn `src/lab13.py` đã sẵn sàng bàn giao cho TV2 làm tiếp `TODO CP4`.
- Các việc phối hợp tiếp theo của TV1 sẽ thực hiện cùng nhóm đúng mốc timeline: góp ý event/ngưỡng đo cho bảng 5 ca (CP3), chạy `yaml.safe_load` và kiểm tra dấu `?` trên `pilot_plan.yaml` (CP4), tham gia chấm chéo Gate 2a (17:00), rà soát checklist tổng hợp (17:45) và tự nộp link repo lên LMS trước 23:59 GMT+7.
