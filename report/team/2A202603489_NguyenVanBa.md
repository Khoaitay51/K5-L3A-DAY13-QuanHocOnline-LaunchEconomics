# Báo cáo cá nhân — Nguyễn Văn Ba · 2A202603489

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Ba
- MSSV: `2A202603489`
- Email:
- Nhóm: `QuanHocOnline` · Lớp `L3A`
- Vai trong nhóm: **TV4 — Người gắn nhãn 2 kiêm giữ hồ sơ**

## 2. Phần việc phụ trách

- **CP3:** gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2), so nhãn với TV3.
- **Hồ sơ launch v0:** giữ và hoàn thiện `report/team/ho_so_launch_v0.md`.
- **Tích hợp và rà soát cuối:** merge nhánh các thành viên vào `main`, chạy checklist nộp bài, sửa lỗi phát hiện được.

## 3. Đóng góp cụ thể

- **Gắn nhãn CP3:** gắn độc lập cột "Nhãn người 2" cho 20 ca trong `bang_loi.md`; trùng 18/20 ca với TV3 (đồng thuận 90,0%), lệch ca 6 và ca 13, thống nhất lại theo nguyên nhân gốc.
- **Tích hợp nhánh:** merge `tranquangnam` (TV3) vào `main`, không có xung đột.
- **Sửa `src/lab13.py`:** lệnh `python lab13.py` bị lỗi `UnicodeEncodeError` trên console Windows (cp1252) ngay ở dòng in phép thử A1. Thêm `sys.stdout.reconfigure(encoding='utf-8')`, chạy lại không cần cờ `-X utf8`, exit code 0.
- **Sửa `ho_so_launch_v0.md`:** điều kiện 3 ghi hai vai phụ trách nên tách thành hai điều kiện, mỗi điều kiện một vai; thêm điều kiện Giám đốc vận hành ký chấp nhận MDE 6 điểm (power 64,17% nếu tác động thật là 5 điểm); sửa câu "ngưỡng hòa vốn 1,03×" thành ngưỡng 4,8 phút/ca và chi phí 12.415 đ = 1,03× (`simulated`).
- **Sửa `bang_chi_phi.md` và `group_report.md`:** thêm lý do loại `doi_tac` (0,85×, `simulated`); sửa câu "đạt 30/30 điểm hội đồng" vì `phieu_cham.md` là phiếu nhóm mình chấm nhóm khác.

## 4. Bằng chứng

- Commit merge `50a4b33` và commit sửa lỗi trên nhánh `main`.
- Kết quả chạy `cd src && python lab13.py`: in `Ba phép thử đáp án biết trước: ĐẠT`, A2 CPS 4.472 đ (`simulated`), D1 1.251 · 3.103 · 1.000 · 300 · m ≥ 299.
- `yaml.safe_load` đọc được `pilot_plan.yaml` (11 trường, 3 luật dừng); không còn dấu `?` ngoài chú thích; không có từ cấm trong `report/team/`.

## 5. Công cụ AI đã dùng

- **Claude Code (trong VS Code):** đọc toàn bộ đề, merge nhánh, chạy script kiểm tra, phát hiện lỗi encoding và các chỗ hồ sơ trái quy tắc, đề xuất và áp dụng sửa.
- **Cách tự kiểm tra:** chạy lại `python lab13.py` trên PowerShell không cờ UTF-8 (exit 0); đối chiếu từng số in ra với bảng số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%); chạy `yaml.safe_load` và `grep` cho dấu `?` và từ cấm. Không dùng AI để gắn nhãn 20 ca lỗi hay điền kết quả duyệt chéo.

## 6. Tự đánh giá

- *(tự điền)*
