# Báo cáo cá nhân — Trần Quang Nam · 2A202603516

Copy từ file mẫu `report/team/MSSV_HoTen.md`.

## 1. Thông tin thành viên

- Họ tên: **Trần Quang Nam**
- MSSV: `2A202603516`
- Email: `wgnam2k4@gmail.com`
- Nhóm: `QuanHocOnline` · Lớp `L3A`
- Vai trong nhóm: **TV3 — Người gắn nhãn 1 & QA / Gatekeeper**

## 2. Phần việc phụ trách

- **Xuyên suốt buổi lab:** Đảm nhiệm vai trò QA / Gatekeeper, giám sát chất lượng toàn bộ deliverables theo Rubric C1–C8; kiểm tra chéo nhãn `simulated` trên mọi số liệu giả lập, quy tắc câu trả lời không quá 3 dòng và có số, quy tắc người phụ trách là một vai trò cụ thể, và tuyệt đối không dùng từ khóa cấm theo Quy tắc 5 (chỉ duyệt kế hoạch pilot, không viết như thể đã chạy chính thức).
- **CP3 (Phân loại lỗi & Khắc phục):** Tự gắn nhãn độc lập toàn bộ 20 ca lỗi theo 5 nhóm Google PAIR trong 8 phút (ngồi tách biệt, không trao đổi); so sánh với Người gắn nhãn 2 (TV4), tính tỉ lệ đồng thuận (đạt 90,0%), viết quy tắc phân biệt cho 2 ca lệch (Ca 6, Ca 13) và chủ trì hoàn thiện bảng khắc phục 5 ca đủ 5 loại có cách phát hiện đo được trong `report/team/bang_loi.md`.
- **CP4 (Kế hoạch pilot):** Hoàn thiện 5 câu D2 kiểm tra "tách được tác động", phân tích đánh đổi MDE 6 điểm (chấp nhận power 64,17% tại 5 điểm), xác lập ngưỡng an toàn dựa trên tỉ lệ mở lại hiện tại (3,97%–4,25%), thiết lập 3 luật dừng định lượng đủ 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`), quy định quy trình rollback 30 phút và xóa sạch dấu `?` trong `report/team/pilot_plan.yaml`.
- **CP5 (Chỉ số, Rủi ro & Hồ sơ Gate 2a):** Đề xuất 1 chỉ số Dùng (% mở gợi ý trợ lý nhóm can thiệp) và 1 chỉ số An toàn (% đơn hoàn sai tiền qua kiểm toán mẫu) trong bảng E1 `report/team/chi_so.md`; phối hợp cùng TV4 rà soát, hoàn thiện và khóa hồ sơ 1 trang `report/team/ho_so_launch_v0.md` phục vụ duyệt chéo Gate 2a lúc 17:00.
- **Duyệt chéo & Đóng gói:** Đại diện nhóm chủ trì chấm phản biện chéo nhóm bạn (PhanDao, Lớp L3A) tại `report/team/phieu_cham.md`, chấm điểm định lượng C6–C8 (đạt 30/30), đặt câu hỏi phản biện sâu và ghi lại câu trả lời tại lớp; chủ trì viết báo cáo nhóm `report/team/group_report.md`; cập nhật thông tin thành viên và ma trận đóng góp trong `TEAM.md`.

## 3. Đóng góp cụ thể

- **Phân loại lỗi 20 ca và bảng khắc phục CP3 ([bang_loi.md](bang_loi.md)):**
  - Gắn nhãn độc lập 20 ca: đạt 18/20 ca trùng với TV4 (tỉ lệ đồng thuận **90,0%** ≥ 80%). Sau khi đối chiếu nguyên nhân gốc, chốt bộ nhãn thống nhất khớp **20/20** đáp án chuẩn của Google PAIR.
  - Viết 2 câu quy tắc phân biệt cho ca không trùng: Ca 6 thuộc *Do người dùng* (khách chọn sai lý do; việc trợ lý thiếu luồng gợi ý thuộc phần khắc phục), Ca 13 thuộc *Giới hạn hệ thống* (bảo hiểm là dịch vụ đối tác ngoài phạm vi trợ lý).
  - Hoàn thiện bảng khắc phục cho 5 ca (Ca 9 - Do người dùng, Ca 7 - Hệ thống, Ca 18 - Ngữ cảnh, Ca 4 - Giới hạn hệ thống, Ca 17 - Ngầm): mọi dòng đều có cách phát hiện đo được (tên event, ngưỡng kích hoạt, chu kỳ), hành động khắc phục cụ thể và một vai trò chịu trách nhiệm rõ ràng.
- **Kế hoạch pilot và 3 luật dừng 4 vế CP4 ([pilot_plan.yaml](pilot_plan.yaml)):**
  - Trả lời đầy đủ 5 câu D2 "tách được tác động" (đối chứng song song 20+20 nhân viên, phân tầng theo depot, bốc thăm ngẫu nhiên với seed=42, kiểm soát rủi ro gián tiếp qua tài khoản cá nhân, công bố trước các chỉ số và có đúng 20 cụm mỗi nhóm).
  - Phân tích và ghi nhận đánh đổi: phương án 20 nhân viên/nhóm chấp nhận MDE 6 điểm phần trăm (`n_hiệu_dụng = 859`, `m ≥ 299`, `DE = 6,96`); nếu tác động thực tế chỉ đạt 5 điểm, power giảm còn **64,17%**.
  - Soạn thảo 3 luật dừng chuẩn cú pháp 4 vế: An toàn (mở lại cao hơn đối chứng ≥ 2 điểm hoặc vượt 6%, hoặc hoàn trùng), Chi phí (CPS > 8.000 đ trong 2 tuần), Mức độ sử dụng (bỏ qua gợi ý > 40% trong 1 tuần); quy định cơ chế rollback bằng feature flag trong vòng 30 phút.
  - Làm sạch toàn bộ dấu `?` trong file YAML, đảm bảo nạp trơn tru qua `yaml.safe_load`.
- **Đặc tả chỉ số và kiểm tra chéo CP5 ([chi_so.md](chi_so.md)):**
  - Đề xuất thêm 1 chỉ số Dùng (*Tỉ lệ mở gợi ý trợ lý trong nhóm can thiệp*) đo bằng `agent_suggestion_shown ÷ refund_request_created` và 1 chỉ số An toàn (*Tỉ lệ sai sót số tiền hoàn qua kiểm toán mẫu*) đo bằng `audit_sample_checked` có `chenh_lech != 0` để phát hiện lỗi ngầm.
  - Cập nhật mục Kiểm tra chéo đảm bảo 100% các chỉ số đều có event và `trace_id` đo lường tương ứng.
- **Hồ sơ launch v0 và Duyệt chéo Gate 2a ([ho_so_launch_v0.md](ho_so_launch_v0.md), [phieu_cham.md](phieu_cham.md)):**
  - Rà soát hồ sơ 1 trang: 7 mục đều có con số định lượng, trạng thái chuẩn (`Giả lập` cho Mục 1, 2, 3, 7; `Xong, có bằng chứng` cho Mục 4, 5, 6), vai trò phụ trách đơn nhất và đề xuất cuối **Go có điều kiện** kèm 3 điều kiện và ngày kiểm tra cụ thể.
  - Chấm chéo nhóm bạn trên `phieu_cham.md` đạt 30/30 điểm (C6: 10đ, C7: 10đ, C8: 10đ) với lý do định lượng có số, đặt câu hỏi về chi phí cố định ở bước rollout 0.10 (khoảng 3.375 việc thành công/tháng, chi phí mỗi việc cộng cố định ≈ 15.266 đ = 1,27× [simulated], dưới điểm hòa vốn khoảng 4.660 việc mà PhanDao tự tính) và ghi nhận câu trả lời của đội bạn trong `phieu_cham.md`.
- **Báo cáo nhóm ([group_report.md](group_report.md)):**
  - Chủ trì tổng hợp báo cáo nhóm ngắn gọn 2 trang, đầy đủ 8 mục tiêu chuẩn, dẫn nguồn tài liệu tham khảo khoa học (Cost-of-Pass, Google PAIR, statsmodels).

## 4. Bằng chứng

- Bảng lỗi và cách khắc phục: `report/team/bang_loi.md`.
- Kế hoạch pilot chuẩn YAML không còn dấu `?`: `report/team/pilot_plan.yaml`.
- Chỉ số đề xuất và kiểm tra chéo: `report/team/chi_so.md`.
- Hồ sơ launch v0 đạt chuẩn 1 trang: `report/team/ho_so_launch_v0.md`.
- Phiếu chấm hội đồng Gate 2a: `report/team/phieu_cham.md`.
- Báo cáo tổng kết nhóm: `report/team/group_report.md`.
- Khai báo vai trò và ma trận đóng góp: `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Antigravity AI Assistant được sử dụng hỗ trợ tra cứu công thức tính hệ số thiết kế cụm (`DE`), đối chiếu cú pháp YAML chuẩn, rà soát ngữ pháp tiếng Việt chuyên ngành kinh tế/AI và hỗ trợ viết các câu lệnh kiểm tra tự động (`yaml.safe_load`, kiểm tra regex dấu `?`, kiểm tra từ cấm).
- **Cách tự kiểm tra kết quả:**
  1. Kiểm tra tính hợp lệ của YAML: chạy lệnh `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml', encoding='utf-8'))"` đảm bảo không phát sinh lỗi parse.
  2. Kiểm tra dấu hỏi sót lại: chạy lệnh `grep -v '^ *#' report/team/pilot_plan.yaml | grep -n '?'` xác nhận không còn bất kỳ dấu `?` nào trong cấu trúc YAML.
  3. Kiểm tra từ cấm và quy tắc vai trò: rà soát đảm bảo không xuất hiện từ cấm theo Quy tắc 5 trong thư mục báo cáo và 100% người phụ trách là một vai trò duy nhất có thẩm quyền.
  4. Kiểm tra tính nhất quán số liệu: đối chiếu chéo toàn bộ các con số chi phí (4.472 đ, 2.696 đ, 8.221 đ, 5.865 đ, 4.599 đ, 11.743 đ, 12.415 đ) giữa `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` và `ho_so_launch_v0.md` đảm bảo khớp 100% với kết quả chạy từ `src/lab13.py`.

## 6. Tự đánh giá

- Đã hoàn thành 100% khối lượng công việc được phân công cho TV3 theo đúng kế hoạch `IMPLEMENTATION_PLAN.md` và các mốc yêu cầu của `CHECKPOINTS.md`.
- Các sản phẩm do TV3 chủ trì hoặc phối hợp thực hiện đều đáp ứng nghiêm ngặt tiêu chí Rubric C1–C8, đảm bảo tính liêm chính học thuật (gắn nhãn độc lập, không sửa bộ nhãn gốc, công khai các con số bất lợi về power và chi phí xem lại).
- Sẵn sàng nộp link repo nhóm lên LMS bằng tài khoản cá nhân trước deadline 23:59 GMT+7.
