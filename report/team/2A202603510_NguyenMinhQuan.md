# Báo cáo cá nhân — Nguyễn Minh Quân · 2A202603510

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Quân
- MSSV: `2A202603510`
- Nhóm: `QuanHocOnline` · Lớp `L3A`
- Vai trong nhóm: TV2, người kiểm số (CP1–CP2) và người viết code chặng 2 (CP4–CP5).

## 2. Phần việc phụ trách

- Đối chiếu kết quả A/B với công thức và hoàn thiện bảng chi phí. Kiểm tra riêng tác động của giới hạn chạy lại và kịch bản xem lại 100% gợi ý.
- Bổ sung phép tính cỡ mẫu D1, power ở mức tác động 5 điểm phần trăm và tỷ lệ mở lại trong 7 ngày. Ghi kết quả và đánh đổi vào `pilot_plan.yaml`.
- Tính ba chỉ số E1 từ CSV và lập bảng E2 về các rủi ro kinh tế cần theo dõi trong pilot.

## 3. Đóng góp cụ thể

- **A1–A4, B1–B4.** Bảng chi phí ghi đủ ba phép thử A1, chi phí theo loại yêu cầu, hai mức khối lượng và chín kịch bản độ nhạy. Giới hạn hai lần chạy cho chi phí cả hệ thống thấp nhất, **6.901.220 đ**. Xem lại 100% gợi ý có thể làm chi phí lên **12.415 đ/việc thành công**, tương đương **1,03×** mức nhân viên tự làm khi dùng trung bình phút làm lại từ CSV. Các kết quả chi phí này có nhãn `simulated`.
- **D1.** Chia theo yêu cầu cần **1.251 yêu cầu mỗi nhóm** để phát hiện chênh lệch 5 điểm. Với 20 nhân viên mỗi nhóm và ICC 0,02, cỡ mẫu hiệu dụng có trần **1.000**. Phương án theo nhân viên chấp nhận mức chênh **6 điểm**, cần ít nhất **299 yêu cầu mỗi người** và có power **64,17%** nếu tác động thật chỉ là 5 điểm.
- **E1 và E2.** Tỷ lệ đóng trong 24 giờ và không mở lại là **82,83%** (994/1.200), tỷ lệ sửa hoặc bỏ gợi ý là **27,12%** (48/177), tỷ lệ mở lại là **4,25%** (51/1.200). Bảng E2 nêu ba rủi ro về làm lại, xem lại toàn bộ và giảm khối lượng, kèm dấu hiệu theo dõi, hành động và vai trò phụ trách.

## 4. Bằng chứng

- [`src/lab13.py`](../../src/lab13.py) in kết quả A/B, D1 và E1 từ dữ liệu gốc.
- [`bang_chi_phi.md`](bang_chi_phi.md) có các bảng A1–A4, B1–B4 và kết luận định lượng.
- [`pilot_plan.yaml`](pilot_plan.yaml) ghi năm câu D1, thiết kế theo nhân viên và tỷ lệ mở lại làm mốc an toàn.
- [`chi_so.md`](chi_so.md) ghi ba tỷ lệ E1 và ba dòng rủi ro E2.

## 5. Công cụ AI đã dùng

- Trợ lý AI lập trình hỗ trợ triển khai phép tính từ công thức của lab, tổng hợp bảng và rà tính nhất quán giữa script, CSV và hồ sơ.
- Cách đối chiếu là chạy `python -X utf8 lab13.py` trong `src/`, đếm lại các tử số và mẫu số E1 trực tiếp từ CSV, rồi đọc kế hoạch pilot bằng `yaml.safe_load`. Các phép tính dưới đây có thể đối chiếu cùng kết quả chạy script.

| Mục | Phép tính đối chiếu |
| --- | --- |
| A1 | Với `p = 0,8` và tối đa 2 lần, số lần chạy kỳ vọng là `1 + 0,2 = 1,20`. |
| A2 | `4.373.585 / 978 ≈ 4.472 đ/việc thành công` (`simulated`). |
| A4 | `40.000.000 / (45.000 × 900 / 1.200) ≈ 1.185 đ` chi phí cố định mỗi việc. Cộng khoảng `3.414 đ` chi phí biến đổi cho ra `4.599 đ` (`simulated`). |
| B2 | `(4.373.585 + 245.585 + 1.780.000) / 978 ≈ 6.543 đ` (`simulated`). |
| B3 | Giới hạn 2 lần cho `4.093.220 + 234 × 12.000 = 6.901.220 đ` (`simulated`). |
| B4 | Với 9 phút làm lại, `(224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900 ≈ 11.743 đ` (`simulated`). |

## 6. Tự đánh giá

- Chi phí mỗi việc thành công và chi phí cả hệ thống trả lời hai câu hỏi khác nhau. Giới hạn một lần có chi phí mỗi việc thành công thấp nhất, còn hai lần giảm tổng chi phí nhờ bớt 85 yêu cầu chuyển sang nhân viên.
- Pilot cần đo phút xem lại và làm lại bằng log. Đồng thời, khi đọc kết quả pilot cần nêu mức chênh 6 điểm mà thiết kế đủ sức phát hiện và power thấp hơn đối với tác động 5 điểm.
