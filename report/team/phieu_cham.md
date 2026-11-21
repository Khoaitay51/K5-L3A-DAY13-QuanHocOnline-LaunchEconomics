# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): `QuanHocOnline` (Lớp `L3A`)
- Nhóm được chấm: `PhanDao` (Lớp `L3A`) · repo `K5-L3A-DAY13-PhanDao-LaunchEconomics`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp số: 4.472 đ/việc, cả hệ thống 0,49×, phạm vi pilot 4.599 đ = 0,38× [simulated]. Nêu thẳng số bất lợi ngay cạnh đề xuất: xem lại 100% lên 11.743–12.415 đ (0,98×–1,03×) [simulated], power 0,64 ở mức +5 điểm, mở lại nền 4,25% (3,97% phạm vi); 4 điều kiện có vai trò và ngày kiểm tra. Điểm trừ nhỏ: điều kiện 4 giữ xem lại ≤ 5,1 phút trong khi chính nhóm tính hòa vốn chỉ 4,8 phút nếu làm lại 15,3 phút. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn `[simulated]` ở mọi số tính từ phút xem lại/làm lại (A2–A4, B1–B4, hồ sơ, E2) và có `simulated_inputs` trong `pilot_plan.yaml`. Thu hẹp về `noi_dia` (0,22×) + `hang_nang` (0,69×); loại `quoc_te` (1,88×, thành công 27,3%, ok tụt 30,0% → 11,4% → 2,2%) và `doi_tac` (0,85×, điều khoản riêng). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, ngẫu nhiên có seed, phân tầng depot, đối chứng cùng tuần; đủ 5 câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96) và nêu đánh đổi MDE 6 điểm, power 0,6417. 3 luật dừng đủ 4 vế, có ngưỡng (+2 điểm/trần 6%/≥ 1 ca trùng; > 8.000 đ hoặc làm lại > 7%; bỏ qua > 40% hoặc mở trợ lý < 50%), thời hạn (3 ngày; 2 tuần; 1 tuần) và người có quyền dừng (Giám đốc vận hành, tắt trong 30 phút). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp số chuẩn, nhãn `simulated` nhất quán, phạm vi thu hẹp có lý do bằng số và pilot tách được tác động. Hai điểm cần bổ sung trước khi mở pilot: (1) chi phí cố định 40 triệu/tháng mới tính ở 45.000 và 22.500 yêu cầu/tháng, chưa tính ở khối lượng thật của từng bước rollout (ở bước 0.10, khoảng 3.375 việc thành công/tháng, dưới điểm hòa vốn khoảng 4.660 việc mà chính nhóm tính); (2) dùng ngưỡng xem lại 4,8 phút thay vì 5,1 phút cho khớp phút làm lại 15,3 phút trong dữ liệu [simulated]. Người phụ trách cả 7 mục của hồ sơ là vai trong nhóm làm lab (Người kiểm số, Người gắn nhãn, Người viết code), chưa phải vai trò có quyền quyết định ở LogiX-VN.

**Một câu hỏi cho đội trình:** Hồ sơ ghi 0,38× ở 45.000 yêu cầu/tháng và chính nhóm tính hòa vốn khi còn khoảng 4.660 việc thành công/tháng. Ở bước rollout 0.10 (4 nhân viên, khoảng 3.375 việc thành công/tháng), chi phí mỗi việc thành công cộng cố định là 3.414 + 40.000.000 / 3.375 ≈ 15.266 đ = 1,27× [simulated]. Luật dừng chi phí 8.000 đ "chưa gồm cố định" có che mất con số này không?

**Câu trả lời của đội trình (ghi lại tại buổi):** *(Tóm tắt theo lập trường trong hồ sơ PhanDao; nhóm sửa lại cho đúng lời đội trình nếu khác.)* Đội trình nhận rằng ở khối lượng nhỏ của bước rollout đầu, chi phí cố định làm chi phí mỗi việc vượt 12.000 đ; đây là lý do A4 đã ghi điểm hòa vốn khoảng 4.660 việc thành công/tháng (khoảng 6.200 yêu cầu/tháng) và nói rõ hồ sơ phải ghi số đã cộng cố định ở khối lượng nào. Luật dừng chi phí cố ý không gồm cố định để đo phần biến đổi mà trợ lý kiểm soát được; chi phí cố định giai đoạn pilot là chi phí học, không dùng để kết luận, và rủi ro khối lượng thấp đã có dòng riêng trong E2 (số việc thành công theo tuần < 50% kế hoạch thì không mở rộng pilot, PM trợ lý hoàn phí phụ trách).
