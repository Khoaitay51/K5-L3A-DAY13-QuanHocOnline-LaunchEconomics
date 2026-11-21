# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Trần Quang Nam (TV3)** · Người gắn nhãn 2: **Nguyễn Minh Quân (TV4)** (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = **90,0%** (đạt ngưỡng yêu cầu ≥ 80%).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận đạt 90,0% (> 80%), hai người đối chiếu nguyên nhân gốc để chốt nhãn thống nhất:

- **Ca 6 (Do người dùng vs Hệ thống):** Gốc lỗi do khách hàng chọn sai mục lý do ("Hoàn phí giao trễ" thay vì hàng bị vỡ) nên xếp vào **Do người dùng**; việc trợ lý thiếu luồng gợi ý đổi danh mục khi phát hiện từ khóa mâu thuẫn là giải pháp cải tiến ở phần khắc phục chứ không phải lỗi hệ thống làm sai chính sách.
- **Ca 13 (Giới hạn hệ thống vs Hệ thống):** Hoàn phí bảo hiểm hàng hóa là nghiệp vụ thuộc đơn vị bảo hiểm đối tác, hoàn toàn nằm ngoài phạm vi chức năng và dữ liệu của trợ lý LogiX nên nguyên nhân gốc là **Giới hạn hệ thống**; câu trả lời chung chung chưa dứt khoát là khuyết điểm xử lý ngoại lệ.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` kèm `field=tracking_code`; cảnh báo kích hoạt khi tỉ lệ vượt quá 2% tổng số yêu cầu/ngày. | Nhận diện mẫu regex mã sàn TMĐT phổ biến và tự động tra cứu sang mã vận đơn LogiX; nếu không tìm thấy thì gửi hướng dẫn kèm ảnh chụp vị trí mã trên bưu gửi. | Quản lý sản phẩm trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: quét toàn bộ tin nhắn "đã hoàn tiền" không có bản ghi sổ cái tương ứng `status == 'ok'` cùng `trace_id`; ngưỡng kích hoạt cảnh báo là > 0 ca. | Chỉ gửi thông báo hoàn tất khi dịch vụ sổ cái trả về HTTP 200 OK; nếu gặp lỗi 503 sau 3 lần retry thì cập nhật trạng thái "đang xử lý" và tự động chuyển sang nhân viên CSKH. | Kỹ sư trưởng Agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại (`ticket_reopened`) vì lý do khiếu nại số tiền trong khi kiểm tra thấy số tiền hoàn đúng chính sách; theo dõi theo chu kỳ tuần qua event `ticket_reopened` nối `trace_id`. | Chuẩn hóa mẫu tin nhắn thông báo hoàn tiền luôn hiển thị chi tiết công thức tính minh bạch: "Cước 30.000 đ × Mức hoàn 50% (trễ > 24h) = 15.000 đ" thay vì chỉ gửi số tiền nhận được. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = 'thieu_du_lieu_doi_tac_quoc_te'` được ghi nhận theo thời gian thực; đo lường theo loại yêu cầu `loai == 'quoc_te'`. | Đưa toàn bộ phạm vi `quoc_te` ra khỏi pilot (do tỉ lệ thành công chỉ đạt 27,3% và chi phí 22.515 đ = 1,88×); giữ nguyên luồng chuyển trực tiếp cho nhân viên kèm tóm tắt thông tin đã thu thập. | Quản lý sản phẩm trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán mẫu ngẫu nhiên 100 đơn/tuần (`audit_sample_checked`) đối chiếu số tiền đã hoàn với bảng giá gốc; ngưỡng cảnh báo kích hoạt khi phát hiện > 1% số đơn có chênh lệch tiền hoàn. | Cơ chế tự động làm mới bộ nhớ đệm (cache invalidation) ngay khi bảng giá có phiên bản mới; gắn `pricing_version` vào metadata của mỗi lần chạy và bắt buộc kiểm tra phiên bản cache trước khi tính tiền. | Kỹ sư hạ tầng dữ liệu |
