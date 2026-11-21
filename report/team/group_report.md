# Báo cáo nhóm · Lab 13: Định giá agent và lập kế hoạch pilot (Gate 2a)

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- **Tên nhóm:** `QuanHocOnline`
- **Lớp:** `L3A`
- **Thành viên:** 4 người (chi tiết phân công và ma trận đóng góp xem tại [TEAM.md](../../TEAM.md)):
  1. Phạm Trường Chinh (MSSV: 2A202603426) — Người viết code (CP1–CP2) → Kỹ sư kiểm chứng & Event (CP3–CP5)
  2. Nguyễn Minh Quân (MSSV: 2A202603510) — Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5)
  3. Trần Quang Nam (MSSV: 2A202603516) — Người gắn nhãn 1 & QA / Gatekeeper
  4. Thành viên 4 (TV4) — Người gắn nhãn 2 kiêm Người giữ hồ sơ (Dossier Owner & Presenter Lead)

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ hồ sơ thẩm định kinh tế và kế hoạch pilot (Gate 2a) cho trợ lý hoàn phí **LogiX-VN** dựa trên tập dữ liệu chạy thử 1.200 yêu cầu (`src/logix_requests.csv`) và 1.624 lần chạy (`src/logix_runs.csv`), giải quyết triệt để 4 câu hỏi cốt lõi:
1. **Có đáng chạy không?** Đo lường chi phí thật cho mỗi việc thành công (CPS) từ trace, bao gồm chi phí token, tool và thời gian nhân viên xem lại/làm lại so với mốc tự làm 12.000 đ.
2. **Nhân viên có dùng không?** Thiết lập bộ chỉ số quan sát (chính, dùng, an toàn) và danh sách event có `trace_id` đo được.
3. **Khi hỏng thì sao?** Phân loại 20 ca lỗi theo 5 nhóm Google PAIR, đạt đồng thuận ≥ 80% và xây dựng ma trận khắc phục đo được có một vai trò chịu trách nhiệm.
4. **Pilot thiết kế thế nào để ra quyết định?** Thiết kế thử nghiệm đối chứng song song, phân tích cỡ mẫu có tính hệ số thiết kế cụm và xây dựng 3 luật dừng định lượng có người bấm nút dừng.

## 3. Giải pháp

Nhóm chia làm 5 chặng thực thi bám sát quy trình và ma trận phân vai Single-Writer:
- **Nhiệm vụ A — Mô hình chi phí ([report/team/bang_chi_phi.md](bang_chi_phi.md)):** Lập trình hàm tính chi phí trong `src/lab13.py`, vượt qua 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`). Tử số cộng toàn bộ lần chạy (kể cả lỗi), mẫu số chỉ đếm 978 việc thành công. Phân tách chi phí theo 4 loại yêu cầu và mô hình hóa chi phí cố định 40 triệu đ/tháng.
- **Nhiệm vụ B — Phân tích độ nhạy ([report/team/bang_chi_phi.md](bang_chi_phi.md)):** Chạy 9 kịch bản độ nhạy B1, phân tích kết hợp B2, so sánh chi phí cả hệ thống theo số lần chạy B3 và kịch bản xem lại 100% B4.
- **Nhiệm vụ C — Phân loại lỗi & Khắc phục ([report/team/bang_loi.md](bang_loi.md)):** Hai người gắn nhãn độc lập 20 ca trong 8 phút, so nhãn tính đồng thuận và lập bảng khắc phục cho 5 ca đại diện đủ 5 nhóm Google PAIR.
- **Nhiệm vụ D — Kế hoạch pilot ([report/team/pilot_plan.yaml](pilot_plan.yaml)):** Giải bài toán cỡ mẫu cụm với `ICC = 0,02`, chọn đơn vị ngẫu nhiên hóa theo nhân viên (20+20), xác định đánh đổi MDE 6 điểm và power 64,17%, ban hành 3 luật dừng 4 vế và quy trình rollback 30 phút.
- **Nhiệm vụ E — Chỉ số, Rủi ro & Hồ sơ Gate 2a ([report/team/chi_so.md](chi_so.md), [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md)):** Chuẩn hóa 10 event có `trace_id`, đo đạc 3 chỉ số chạy thử và 2 chỉ số tự đề xuất, kiểm soát rủi ro kinh tế và đóng gói hồ sơ 1 trang.

## 4. Kết quả

- **Chi phí thật:** CPS toàn mẫu là **4.472 đ** (`simulated`), gấp **16,3 lần** hóa đơn token+tool (274,7 đ). Thời gian làm lại (2.264.000 đ, 51,8%) và xem lại (1.780.000 đ, 40,7%) chiếm tới 92,5% tổng chi phí. Cả hệ thống tốn **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ (`simulated`).
- **Phạm vi tối ưu:** Thu hẹp pilot về `noi_dia` (**2.696 đ = 0,22×**, `simulated`) và `hang_nang` (**8.221 đ = 0,69×**, `simulated`). Loại bỏ `quoc_te` (22.515 đ = 1,88×, thành công chỉ 27,3%) và `doi_tac` (10.215 đ = 0,85×). Ở quy mô 45.000 yc/tháng kèm 40 triệu cố định, CPS trong phạm vi đạt **4.599 đ = 0,38×** (`simulated`).
- **Giới hạn chạy lại:** Giới hạn 2 lần chạy là tối ưu nhất cho toàn công ty (**6.901.220 đ**), rẻ hơn chạy 3 lần (7.037.585 đ) và chạy 1 lần (7.449.781 đ do đẩy 319 ca sang nhân viên).
- **Phân loại lỗi:** Đạt tỉ lệ đồng thuận độc lập **90,0%** (18/20 ca), thống nhất khớp **20/20** đáp án chuẩn Google PAIR.
- **Kế hoạch pilot:** Chia 20 nhân viên can thiệp vs 20 nhân viên đối chứng song song trên 12 depot. Cỡ mẫu hiệu dụng tối thiểu **859 yêu cầu/nhóm** (quan sát **5.980 yêu cầu/nhóm**, `m ≥ 299`, `DE = 6,96`).
- **Đề xuất cuối:** **Go có điều kiện** (chỉ mở pilot khi thu hẹp phạm vi về `noi_dia + hang_nang`, vá 5 lỗi kỹ thuật cốt lõi và kiểm soát thời gian xem lại ≤ 4,8 phút/ca trong tuần đầu).
- **Kết quả duyệt chéo Gate 2a:** Đạt **30/30 điểm** hội đồng từ nhóm chấm chéo ([report/team/phieu_cham.md](phieu_cham.md)).

## 5. Khó khăn và cách xử lý

1. **Hiệu ứng cụm làm suy giảm cỡ mẫu hiệu dụng:** Với `ICC = 0,02`, việc chia theo 6 depot cho trần hiệu dụng chỉ 300 (< 1.251 yêu cầu cần thiết); chia 20 nhân viên cũng có trần hiệu dụng 1.000.  
   *Cách xử lý:* Chấp nhận nới MDE lên 6 điểm phần trăm (cần 859 hiệu dụng, `m ≥ 299`), đồng thời công khai minh bạch con số bất lợi: power giảm còn **64,17%** nếu tác động thực chỉ đạt 5 điểm.
2. **Kịch bản xem lại 100% có nguy cơ lỗ:** Nếu phải duyệt 100% gợi ý và thời gian làm lại trung bình là 15,30 phút (từ CSV), CPS đội lên **12.415 đ = 1,03×** (đắt hơn tự làm).  
   *Cách xử lý:* Tính toán ngưỡng hòa vốn bắt buộc cho thời gian xem lại là **≤ 4,8 phút/ca**, đưa vào điều kiện tiên quyết và thiết lập luật dừng chi phí > 8.000 đ.
3. **Phân biệt lỗi Ngầm và lỗi Hệ thống:** Dễ nhầm lẫn các ca sai lệch trích dẫn hoặc bảng giá cũ.  
   *Cách xử lý:* Thống nhất nguyên tắc: lỗi Hệ thống là lỗi vi phạm đã lộ ra và có người thấy; lỗi Ngầm là lỗi không ai nhận ra (kể cả khách và hệ thống) cho tới khi kiểm toán mẫu.

## 6. Tổng hợp đóng góp

| Thành viên | Vai trò | Đóng góp chính |
| --- | --- | --- |
| Phạm Trường Chinh (TV1) | Người viết code chặng 1 → Kỹ sư kiểm chứng | Lập trình A1–A4, B1–B4 trong `src/lab13.py`; thiết kế 10 event có `trace_id` trong `chi_so.md`; lập kế hoạch triển khai. |
| Nguyễn Minh Quân (TV2) | Người kiểm số → Người viết code chặng 2 | Kiểm số bảng chi phí A/B; lập trình tính toán cỡ mẫu D1 và chỉ số E1 trong `src/lab13.py`; xây dựng bảng rủi ro kinh tế E2. |
| Trần Quang Nam (TV3) | Người gắn nhãn 1 & QA / Gatekeeper | Gắn nhãn độc lập 20 ca lỗi CP3; hoàn thiện 5 câu D2 và 3 luật dừng 4 vế trong `pilot_plan.yaml`; đề xuất 2 chỉ số mới; viết `phieu_cham.md` và `group_report.md`. |
| Thành viên 4 (TV4) | Người gắn nhãn 2 kiêm Giữ hồ sơ | Gắn nhãn độc lập 20 ca lỗi CP3; chủ trì hoàn thiện hồ sơ 1 trang `ho_so_launch_v0.md`; đại diện trình bày và phản biện Gate 2a. |

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian xem lại/làm lại còn ở dạng giả lập (`simulated`):** Khi bước vào tuần 1 của pilot, nhóm cần thay thế ngay bằng số liệu đo lường thực tế từ event `staff_review_decision` và `staff_rework_completed` để cập nhật lại mô hình kinh tế.
- **Power chưa đạt 80% ở mức chênh 5 điểm:** Cần theo dõi chặt chẽ phương sai giữa các nhân viên trong quá trình rollout; nếu mức độ tương quan nội cụm thực tế nhỏ hơn 0,02 (`ICC < 0,02`), power sẽ tự động cải thiện.

## 8. Tài liệu tham khảo

1. Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arXiv:2504.13359](https://arxiv.org/abs/2504.13359).
2. Google PAIR, *People + AI Guidebook*, Chapter "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
3. Statsmodels Development Team, `NormalIndPower` documentation for proportion tests, Python `statsmodels.stats.power`.
