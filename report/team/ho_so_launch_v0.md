# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: `QuanHocOnline` · Lớp: `L3A`

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu (`simulated`); 2.696 đ (`noi_dia`) và 8.221 đ (`hang_nang`) (`simulated`); ở quy mô 45.000 yc/tháng kèm 40tr cố định là 4.599 đ (0,38× so với 12.000 đ, `simulated`). Gấp 16,3 lần hóa đơn token+tool (274,7 đ). | Giả lập | Kỹ sư trưởng Agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% khi x2, lên 6.787 đ); 2. Tỉ lệ xem lại (+40,7% khi x2, lên 6.292 đ); 3. Lương nhân viên (+23,1% khi +25%, lên 5.506 đ) (`simulated`). | Giả lập | Chuyên viên phân tích tài chính |
| 3 · So với nhân viên tự làm | Cả hệ thống tốn 5.865 đ/yêu cầu = 0,49× mức 12.000 đ (tính cả 222 ca chuyển/làm lại) (`simulated`). Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) (`simulated`). | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (994/1.200); Dùng: 27,12% bỏ qua gợi ý (48/177); An toàn: 4,25% lỗi lọt đến khách (51/1.200 toàn mẫu) và 3,97% trong phạm vi `noi_dia` + `hang_nang`. Đủ 10 event có `trace_id`. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi đạt 90,0% đồng thuận (18/20), 20/20 khớp đáp án chuẩn Google PAIR. Bảng khắc phục 5 ca đủ 5 loại có event đo được, ngưỡng định lượng và một vai trò chịu trách nhiệm. | Xong, có bằng chứng | Quản lý sản phẩm trợ lý hoàn phí |
| 6 · Pilot plan | Đối chứng 20+20 nhân viên song song (12 depot); MDE 6 điểm (859 n_hiệu_dụng, m ≥ 299 yc/người, DE = 6,96); chấp nhận power 64,17% nếu tác động thật là 5 điểm; 3 luật dừng 4 vế, rollback 30 phút. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại x2 tăng +51,8% (6.787 đ); xem lại 100% tốn 11.743 đ (0,98×) đến 12.415 đ (1,03× - đắt hơn người tự làm) (`simulated`); khối lượng giảm 50% tăng chi phí cố định lên 5.784 đ (0,48×) (`simulated`). | Giả lập | Giám đốc tài chính |

**Đề xuất:** **Go có điều kiện** (chỉ mở pilot giới hạn sau khi thỏa mãn 3 điều kiện tiên quyết):

1. **Thu hẹp phạm vi pilot:** Chỉ hỗ trợ `noi_dia` (0,22×) và `hang_nang` (0,69×); loại bỏ hoàn toàn `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×) để chuyển nhân viên xử lý thủ công. *Người phụ trách:* Quản lý sản phẩm trợ lý hoàn phí. *Ngày kiểm tra:* 2026-12-01.
2. **Khắc phục lỗi hệ thống cốt lõi trước khi bấm nút:** Tích hợp khóa chống hoàn trùng (Ca 20), xác thực giao dịch sổ cái HTTP 200 trước khi báo thành công (Ca 7), cơ chế xóa cache khi đổi bảng giá (Ca 17), chuẩn hóa tin nhắn nêu rõ công thức tính (Ca 18). *Người phụ trách:* Kỹ sư trưởng Agent. *Ngày kiểm tra:* 2026-12-05.
3. **Kiểm soát thời gian xem lại và ngưỡng an toàn trong tuần 1:** Đảm bảo thời gian xem lại thực tế ≤ 4,8 phút/ca để không bị vượt chi phí nhân viên tự làm (ngưỡng hòa vốn 1,03×); kích hoạt luật dừng an toàn nếu tỉ lệ mở lại cao hơn đối chứng ≥ 2 điểm phần trăm hoặc vượt 6% tuyệt đối. *Người phụ trách:* Trưởng nhóm CSKH & Giám đốc vận hành. *Ngày kiểm tra:* 2026-12-15.
