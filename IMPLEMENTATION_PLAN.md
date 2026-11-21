# Kế hoạch triển khai Lab 13 — Nhóm 4 người (`QuanHocOnline` · Lớp `L3A`)

**Đề tài:** Định giá agent và lập kế hoạch pilot — Trợ lý hoàn phí **LogiX-VN (Gate 2a)**  
**Repo nhóm:** `K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` · **Lớp:** `L3A` · **Hình thức:** Nhóm 4 người  
**Thời lượng tại lớp:** 4 giờ (`14:00–18:00`, giải lao `15:20–15:35`) · **Dữ liệu:** Giả lập hoàn toàn, chạy offline không cần API key.

---

## 1. Tổng quan Lab 13 & Mục tiêu điểm số (100 điểm)

### Bối cảnh bài toán
- **LogiX-VN** có **12 depot**, khoảng **40 nhân viên CSKH**, tiếp nhận khoảng **45.000 yêu cầu hoàn phí/tháng** (1.500 yêu cầu/ngày).
- Trợ lý hoàn phí vừa chạy thử **2 tuần tại 6 depot**. Nhóm nhận mẫu ngẫu nhiên gồm **1.200 yêu cầu** (`src/logix_requests.csv`) và **1.624 lần chạy agent** (`src/logix_runs.csv`).
- Toàn bộ hồ sơ phải trả lời rõ ràng **4 câu hỏi cốt lõi**:
  1. **Có đáng chạy không?** Chi phí thật cho mỗi việc thành công, so với nhân viên tự làm (12.000 đ / 6 phút).
  2. **Nhân viên có dùng không?** Chỉ số sử dụng, tỉ lệ bỏ qua gợi ý và danh sách event có `trace_id`.
  3. **Khi hỏng thì sao?** Phân loại 20 ca lỗi theo 5 nhóm Google PAIR và bảng khắc phục đo được có người phụ trách.
  4. **Pilot thiết kế thế nào để ra được quyết định?** Có nhóm đối chứng song song, đủ cỡ mẫu (hoặc đánh đổi minh bạch), và luật dừng viết trước.

### Cơ cấu điểm Rubric (Tổng 100 điểm · Không có bonus)
Sai số số liệu chấp nhận trong phạm vi **≤ 2%** so với đáp án chuẩn.

| Nhóm tiêu chí | Nội dung | Điểm | Bằng chứng chấm |
| --- | --- | ---: | --- |
| **C1 (CP1)** | Nhiệm vụ A: mô hình chi phí | **20** | `src/lab13.py` in ba phép thử `ĐẠT` (1,20 · 1,25 · 1,25); bảng A2, A3 trong `report/team/bang_chi_phi.md` (có nhãn `simulated`) |
| **C2 (CP2)** | Nhiệm vụ B: bảng độ nhạy | **15** | Bảng B1 (9 dòng), B2 (đổi cặp + xếp hạng 3 yếu tố), B3, B4 trong `report/team/bang_chi_phi.md` |
| **C3 (CP3)** | Nhiệm vụ C: bảng lỗi & khắc phục | **10** | `report/team/bang_loi.md`: 2 bộ nhãn độc lập, đồng thuận ≥ 80%, khớp đáp án ≥ 16/20, bảng 5 ca đủ 5 loại |
| **C4 (CP4)** | Nhiệm vụ D: `pilot_plan.yaml` | **15** | `report/team/pilot_plan.yaml`: chú thích D1/D2, đọc được bằng `yaml.safe_load`, không còn `?`, ≥ 3 luật dừng đủ 4 vế |
| **C5 (CP5)** | Nhiệm vụ E: chỉ số, event, rủi ro, hồ sơ | **10** | `report/team/chi_so.md` & `report/team/ho_so_launch_v0.md` (3 chỉ số, ≥ 6 event có `trace_id`, ≥ 2 rủi ro, 7 mục) |
| **C6 (Hội đồng)** | Đề xuất khớp bằng chứng | **10** | `ho_so_launch_v0.md` + phiếu hội đồng: nêu cả **con số bất lợi** và cách xử lý mới được trọn 10đ |
| **C7 (Hội đồng)** | Số giả lập & phạm vi thu hẹp | **10** | Gắn nhãn `simulated` ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số |
| **C8 (Hội đồng)** | Pilot ra được quyết định | **10** | Tách được tác động (đối chứng cùng thời gian), đủ mẫu, luật dừng có ngưỡng + thời hạn + người có quyền dừng |
| **Tổng** | **70đ đối chiếu + 30đ hội đồng** | **100** | |

### 3 Mốc thời gian bắt buộc
1. **17:00 (tại lớp):** `report/team/ho_so_launch_v0.md` đủ 7 mục + dòng đề xuất cuối để gửi cho nhóm hội đồng duyệt chéo Gate 2a.
2. **17:45–18:00 (tại lớp):** Hoàn thiện báo cáo nhóm & cá nhân, chạy kiểm tra toàn bộ checklist, `commit` và `push` lên repo nhóm.
3. **Trước 23:59 GMT+7 ngày lab (Deadline LMS):** **Mỗi thành viên tự nộp cùng một link repo nhóm trên LMS bằng tài khoản cá nhân.** Ai không nộp link trên LMS sẽ không có điểm dù nhóm đã đẩy code.

---

## 2. Danh sách toàn bộ Deliverables (13 file phải nộp & File cấm sửa)

### 13 file cần hoàn thiện và nộp
| STT | Đường dẫn | Nhiệm vụ | Yêu cầu nội dung bắt buộc | Chủ sở hữu chính |
| --: | --- | --- | --- | --- |
| 1 | `src/lab13.py` | A, B, D1, E1 | Chạy `python3 lab13.py` từ `src/` in ra phép thử `ĐẠT`, A2, A3, A4, B1–B4, D1 và số liệu E1 | TV1 (CP1–CP2) → TV2 (CP4–CP5) |
| 2 | `report/team/bang_chi_phi.md` | A, B | Đủ A1, A2 (9 dòng, nhãn `simulated`), A3 (4 dòng), A4 (2 mức khối lượng), B1 (9 dòng), B2 (xếp hạng), B3, B4 (cả 2 mức phút làm lại) | TV2 (kiểm số) & TV1 |
| 3 | `report/team/bang_loi.md` | C | 2 bộ nhãn độc lập 20 ca, tỉ lệ đồng thuận, quy tắc các ca không trùng, bảng khắc phục 5 ca đủ 5 loại có cách phát hiện đo được & 1 vai trò | TV3 & TV4 |
| 4 | `report/team/pilot_plan.yaml` | D | Phần chú thích đầu file ghi đủ D1 (5 câu) & D2 (5 câu) + đánh đổi + tỉ lệ mở lại; các trường YAML không còn `?`; ≥ 3 luật dừng mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ` | TV2, TV3 & TV1 |
| 5 | `report/team/chi_so.md` | E1, E2 | 3 chỉ số tính thử + 1 Dùng & 1 An toàn tự đề xuất; ≥ 6 event có `trace_id` + kiểm tra chéo event ↔ chỉ số; ≥ 2 dòng rủi ro lấy số từ bảng độ nhạy | TV1, TV2 & TV3 |
| 6 | `report/team/ho_so_launch_v0.md` | E3 | **Đúng 1 trang**, 7 mục (số chính + trạng thái chỉ nhận `Xong, có bằng chứng` / `Chưa` / `Giả lập` + 1 vai trò phụ trách); dòng cuối: `Go` / `Go có điều kiện` / `No-go` | TV4 (giữ hồ sơ) |
| 7 | `report/team/phieu_cham.md` | Duyệt chéo | Phiếu nhóm mình chấm nhóm `n + 1`: điểm từng tiêu chí C6–C8 (0/5/10), lý do có số, quyết định, 1 câu hỏi và ghi lại câu trả lời tại buổi | TV3 & cả nhóm |
| 8 | `TEAM.md` | Hành chính | Tên nhóm, lớp, URL repo/nhánh/commit chốt, bảng 4 thành viên & vai trò, tóm tắt đóng góp & bằng chứng từng người | TV4 & TV3 |
| 9 | `report/team/group_report.md` | Tổng kết | Báo cáo nhóm ngắn ≤ 2 trang, đủ 8 mục theo mẫu có sẵn | TV3 |
| 10–13 | `report/team/<MSSV>_<HoTen>.md` | Cá nhân (×4) | Copy từ `report/team/MSSV_HoTen.md` (không dấu, ví dụ `20241234_NguyenVanAn.md`), ghi rõ phần việc, bằng chứng commit/file, **công cụ AI đã dùng & cách tự kiểm tra** | TV1, TV2, TV3, TV4 (tự viết file của mình) |

### Quy tắc bảo vệ file gốc & dữ liệu
- **TUYỆT ĐỐI KHÔNG SỬA:** `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`, `report/team/MSSV_HoTen.md` (giữ nguyên file mẫu để tham chiếu/copy).
- **TUYỆT ĐỐI KHÔNG COMMIT:** `.venv/`, `venv/`, `.env`, `.env.*`, `__pycache__/`, `*.py[cod]`, hay bất kỳ API key / mật khẩu nào.
- **KHÔNG ĐƯA FILE NGOÀI LUỒNG VÀO `report/team/`:** Giữ nguyên đúng tên các file nộp quy định trong `report/team/`.

---

## 3. Phân công chi tiết cho nhóm 4 người & Ma trận quyền sở hữu file

Áp dụng đúng 4 vai chuẩn trong `TEAM.md` và quy định **bắt buộc đổi người viết code sau giờ giải lao (15:35)** để ít nhất 2 thành viên tự tay lập trình, chạy mô hình và kiểm chứng số liệu.

### Vai trò 4 thành viên

#### TV1 — Người viết code chặng 1 (CP1–CP2) → Kỹ sư kiểm chứng & Event (CP3–CP5)
- **CP0–CP2 (`14:00–15:20`):** Dựng `.venv` trên máy 1; lập trình `src/lab13.py` cho Nhiệm vụ **A1, A2, A3, A4** và **B1, B2, B3, B4**; xuất bảng ra terminal cho TV2 đối chiếu; push `src/lab13.py` và bàn giao quyền code cho TV2 vào lúc giải lao `15:20`.
- **CP3 (`15:35–16:08`):** Hỗ trợ TV2 hoàn thiện phần trình bày trong `report/team/bang_chi_phi.md` trong 8 phút TV3/TV4 đang gắn nhãn độc lập; sau đó rà giúp câu lệnh/ngưỡng đo hệ thống cho bảng khắc phục 5 ca (event, log, idempotency).
- **CP4–CP5 (`16:08–17:00`):** Thiết kế danh sách **6–10 event có `trace_id`** và bảng **kiểm tra chéo event ↔ chỉ số** trong `report/team/chi_so.md`; chạy kiểm chứng kỹ thuật cho `pilot_plan.yaml` (`yaml.safe_load`, `grep '?'`, kiểm tra từ cấm trong `report/team/`).
- **Cuối buổi:** Viết báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md` và chạy kiểm tra cuối cùng trên Git.

#### TV2 — Người kiểm số (CP1–CP2) → Người viết code chặng 2 (CP4–CP5)
- **CP0–CP2 (`14:00–15:20`):** Cài `.venv` trên **máy thứ 2** (đảm bảo yêu cầu checklist chạy hết trên máy khác trong nhóm); tính tay đối chiếu ít nhất 1 phép tính mỗi phần (A1, A2, A4, B2, B3, B4) để bắt lỗi sai công thức/làm tròn ≤ 2%; giữ quyền ghi chính file `report/team/bang_chi_phi.md` (mọi câu trả lời ≤ 3 dòng và có số).
- **CP3 (`15:35–16:08`):** Chốt sạch `report/team/bang_chi_phi.md` và chuẩn bị trước khung tính cỡ mẫu D1 trong `src/lab13.py` (sau khi pull code CP2 từ TV1).
- **CP4 (`16:08–16:36`):** Nhận vai **Người viết code**, viết phần **TODO CP4** trong `src/lab13.py` (tính 5 câu **D1**, tính power thực khi tác động là 5 điểm ở `n = 859`, tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại); đồng chủ trì điền số và chú thích D1 vào `report/team/pilot_plan.yaml`.
- **CP5 (`16:36–17:00`):** Tính thử 3 chỉ số **E1** bằng `src/lab13.py`, viết bảng **E1** (phần tính thử) và **E2** (≥ 2 dòng rủi ro kinh tế lấy số trực tiếp từ B1/B4/A4) vào `report/team/chi_so.md`.
- **Cuối buổi:** Viết báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

#### TV3 — Người gắn nhãn 1 & QA / Gatekeeper
- **Xuyên suốt (`14:00–17:00`):** Nắm chuẩn Rubric C1–C8 và điều kiện "Xong khi" của từng checkpoint; bấm giờ để không lố mốc `17:00`; kiểm tra chéo nhãn `simulated`, câu trả lời ≤ 3 dòng, và không ghi người phụ trách là `"cả đội"`.
- **CP1–CP2:** Đọc kỹ đề bài & `docs/du_lieu_va_cong_thuc.md`, dựng khung `TEAM.md` và sẵn sàng phần đọc hiểu 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi").
- **CP3 (`15:35–16:08`):** Ngồi **tách riêng TV4**, gắn nhãn độc lập toàn bộ 20 ca trong **8 phút không trao đổi**; sau 8 phút mới so với TV4, tính tỉ lệ đồng thuận, **giữ nguyên 2 bộ nhãn gốc**, viết quy tắc phân biệt các ca lệch, và chủ trì hoàn thiện `report/team/bang_loi.md` (5 ca đủ 5 loại Google PAIR).
- **CP4–CP5 (`16:08–17:00`):** Viết **5 câu D2** ("tách được tác động") và **3 luật dừng đủ 4 vế** (`NẾU – TRONG – THÌ – KHÔNG THÌ`) vào `report/team/pilot_plan.yaml`; đề xuất thêm **1 chỉ số Dùng + 1 chỉ số An toàn** trong `report/team/chi_so.md`; rà soát tiêu chí Hội đồng C6–C8 trước 17:00.
- **Duyệt chéo & Đóng gói (`17:00–18:00`):** Chủ trì điền `report/team/phieu_cham.md` khi chấm nhóm `n + 1`; chủ trì viết `report/team/group_report.md`; viết báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

#### TV4 — Người gắn nhãn 2 kiêm Người giữ hồ sơ (Dossier Owner & Presenter Lead)
- **Xuyên suốt (`14:10–17:00`):** Là người giữ quyền ghi duy nhất đối với `report/team/ho_so_launch_v0.md`. **Điền cuốn chiếu ngay từ 14:10**, không dồn sang 16:36:
  - Xong CP1 → điền **Mục 1** (Chi phí mỗi việc thành công) & **Mục 3** (So với nhân viên tự làm).
  - Xong CP2 → điền **Mục 2** (3 yếu tố nhạy nhất) & nháp **Mục 7** (Rủi ro kinh tế từ B1/B4).
  - Xong CP3 → điền **Mục 5** (Bảng lỗi & khắc phục).
  - Xong CP4 → điền **Mục 6** (Pilot plan & đánh đổi).
  - Xong CP5 → điền **Mục 4** (Chỉ số), chốt **Mục 7** và **Đề xuất cuối** (`Go` / `Go có điều kiện` / `No-go`), kiểm soát trang hồ sơ gói gọn **1 trang**.
- **CP3 (`15:35–16:08`):** Ngồi **tách riêng TV3**, gắn nhãn độc lập 20 ca trong **8 phút không trao đổi**, sau đó so nhãn và cùng TV3 chốt bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **Duyệt chéo (`17:00–17:45`):** Gửi `ho_so_launch_v0.md` (và các file liên quan) cho nhóm hội đồng đúng **17:00**; đại diện nhóm trình bày **1 phút** và trả lời phản biện **1 phút**; ghi chú phản hồi của hội đồng.
- **Cuối buổi (`17:45–18:00`):** Hoàn thiện bảng đóng góp trong `TEAM.md`, viết báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`, xác nhận cả 4 thành viên đã tự nộp link trên LMS.

### Ma trận Single-Writer (Chống conflict khi làm song song)
Mỗi file tại một thời điểm chỉ có **1 người chịu trách nhiệm ghi trực tiếp (Writer)**; người còn lại review/gửi số liệu qua chat hoặc đọc từ máy Writer:

| File | CP0–CP2 (14:00–15:35) | CP3 (15:35–16:08) | CP4 (16:08–16:36) | CP5 (16:36–17:00) | Duyệt chéo & Đóng gói (17:00–18:00) |
| --- | --- | --- | --- | --- | --- |
| `src/lab13.py` | **TV1** | *Freeze / TV2 chuẩn bị D1* | **TV2** | **TV2** | *Chỉ sửa nếu fix bug* |
| `report/team/bang_chi_phi.md` | **TV2** | **TV2** (hoàn thiện 8p đầu) | *Freeze* | *Freeze* | *Freeze* |
| `report/team/bang_loi.md` | — | **TV3** (nhận nhãn từ TV4) | *Freeze* | *Freeze* | *Freeze* |
| `report/team/pilot_plan.yaml` | — | — | **TV3** (chú thích/luật) → **TV2** (số D1) | **TV1** (verify YAML) | *Freeze* |
| `report/team/chi_so.md` | — | — | — | **TV1** (events) → **TV2** (bảng E1/E2) | *Freeze* |
| `report/team/ho_so_launch_v0.md` | **TV4** (điền cuốn chiếu) | **TV4** | **TV4** | **TV4** | **TV4** (chỉ chỉnh nếu bổ sung) |
| `report/team/phieu_cham.md` | — | — | — | — | **TV3** |
| `report/team/group_report.md` | — | — | — | — | **TV3** |
| `TEAM.md` | **TV3** (khung) | — | — | — | **TV4** (chốt đóng góp) |
| `report/team/<MSSV>_<HoTen>.md` | — | — | — | — | **Mỗi người tự viết file riêng** |

---

## 4. Timeline chi tiết cho nhóm 4 người (14:00–18:00 + Hạn 23:59 LMS)

> **Lưu ý co giãn giờ:** Nếu buổi lab bắt đầu lệch giờ `14:00`, cả nhóm bám theo cột **Mốc tương đối (`T+...`)** để giữ đúng tỷ lệ thời gian. Mốc vàng không được trễ là **17:00 (`T+180p`)** phải có `ho_so_launch_v0.md` để duyệt chéo.

| Giờ chuẩn | Mốc `T+` | Thời lượng | Giai đoạn / Checkpoint | TV1 | TV2 | TV3 | TV4 | Sản phẩm & Mốc Git |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| `14:00–14:10` | `T+00`–`T+10` | 10p | **Khởi động & Setup** | Tạo `.venv` máy 1, chạy thử `lab13.py` | Tạo `.venv` máy 2, đọc `du_lieu_va_cong_thuc.md` | Điền khung `TEAM.md`, chuẩn bị checklist | Mở khung `ho_so_launch_v0.md`, đọc đề 4 câu | Commit `chore(setup)` (`TEAM.md`) |
| `14:10–14:50` | `T+10`–`T+50` | 40p | **CP1 · Nhiệm vụ A** | Code A1 (10p) → A2 (20p) → A3, A4 (10p) trong `lab13.py` | Tính tay kiểm chứng A1–A4, điền A1–A4 vào `bang_chi_phi.md` | Kiểm tra nhãn `simulated`, kiểm câu ≤ 3 dòng | Điền cuốn chiếu **Mục 1 & Mục 3** của `ho_so_launch_v0.md` | `src/lab13.py` (A1–A4), `bang_chi_phi.md` (phần A) |
| `14:50–14:53` | `T+50`–`T+53` | 3p | **CP1 · Chữa bài & Commit** | Đối chiếu slide đáp án (lệch ≤ 2%), fix nếu lệch | Chốt số A2–A4 | Xác nhận 3 phép thử `ĐẠT` | Cập nhật số chuẩn vào Mục 1 & 3 | Commit & push `feat(cp1)` |
| `14:53–15:18` | `T+53`–`T+78` | 25p | **CP2 · Nhiệm vụ B** | Code B1 (12p) → B2, B3, B4 (13p) trong `lab13.py` | Tính tay kiểm B2, B3, B4 (cả 9p & 15,3p), điền phần B vào `bang_chi_phi.md` | Soát xếp hạng top 3 & quy tắc ≤ 3 dòng | Điền cuốn chiếu **Mục 2** & nháp **Mục 7** của `ho_so_launch_v0.md` | `bang_chi_phi.md` đủ B1–B4 |
| `15:18–15:20` | `T+78`–`T+80` | 2p | **CP2 · Chữa bài & Commit** | Đối chiếu slide B1–B4 | Chốt số B1–B4 | Verify bảng độ nhạy | Cập nhật Mục 2 | Commit & push `feat(cp2)` |
| `15:20–15:35` | `T+80`–`T+95` | **15p** | **Giải lao & Đổi vai code** | Push sạch `src/lab13.py`, nghỉ ngơi | Pull `src/lab13.py`, chạy thử xác nhận chạy tốt trên máy 2 | Nghỉ, chuẩn bị file đề `.docx` (20 ca lỗi) cho 2 người gắn nhãn | Nghỉ, chuẩn bị file đề `.docx` tách riêng khỏi TV3 | Bàn giao vai **Người viết code** sang **TV2** |
| `15:35–15:43` | `T+95`–`T+103` | 8p | **CP3 (Bước 1) · Gắn độc lập** | Hỗ trợ rà soát `bang_chi_phi.md` | Chốt sạch `bang_chi_phi.md`, chuẩn bị hàm `co_mau` cho D1 | **Ngồi tách riêng**, tự gắn 20 ca lỗi (không trao đổi) | **Ngồi tách riêng**, tự gắn 20 ca lỗi (không trao đổi) | 2 bộ nhãn độc lập nguyên bản |
| `15:43–15:51` | `T+103`–`T+111` | 8p | **CP3 (Bước 2–3) · So nhãn** | Góp ý nguyên nhân hệ thống/kỹ thuật | Chạy thử nháp D1 trong khi chờ | So nhãn với TV4, tính đồng thuận ≥ 80%, ghi quy tắc ca lệch vào `bang_loi.md` | Đọc lại các ca lệch, thống nhất nhãn chung (giữ nguyên cột gốc) | Hoàn tất 20 ca + tỉ lệ đồng thuận |
| `15:51–16:05` | `T+111`–`T+125` | 14p | **CP3 (Bước 4) · Bảng 5 ca** | Góp ý cách phát hiện đo được (event, ngưỡng) | Rà kiểm số liệu liên quan | Điền bảng khắc phục 5 ca (đủ 5 loại, 1 vai trò/dòng) | Điền cuốn chiếu **Mục 5** của `ho_so_launch_v0.md` | `report/team/bang_loi.md` hoàn chỉnh |
| `16:05–16:08` | `T+125`–`T+128` | 3p | **CP3 · Chữa bài & Commit** | Đối chiếu đáp án | Verify | Soát khớp ≥ 16/20 ca & sửa ghi chú thống nhất (không sửa bộ gốc) | Cập nhật Mục 5 | Commit & push `feat(cp3)` |
| `16:08–16:20` | `T+128`–`T+140` | 12p | **CP4 (D1) · Tính cỡ mẫu** | Kiểm tra công thức `DE` & `power` | Code D1 (5 câu a–e) + power 0,64 + tỉ lệ `mo_lai_trong_7_ngay` trong `lab13.py` | Chuẩn bị 5 câu D2 và nháp 3 luật dừng | Chuẩn bị khung Mục 6 của hồ sơ | Output D1 chuẩn |
| `16:20–16:33` | `T+140`–`T+153` | 13p | **CP4 (D2–D3) · Chốt YAML** | Chạy `yaml.safe_load` & `grep '?'` kiểm lỗi YAML | Điền số D1, `n_per_arm`, `design_effect`, `simulated_inputs` vào `pilot_plan.yaml` | Điền D2, đánh đổi, 3 luật dừng 4 vế vào `pilot_plan.yaml` | Điền cuốn chiếu **Mục 6** (nhấn mạnh đánh đổi & power 0,64) | `report/team/pilot_plan.yaml` sạch dấu `?` |
| `16:33–16:36` | `T+153`–`T+156` | 3p | **CP4 · Chữa bài & Commit** | Xác nhận `yaml.safe_load` ok | Đối chiếu slide D1 | Verify đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ` | Cập nhật Mục 6 | Commit & push `feat(cp4)` |
| `16:36–16:46` | `T+156`–`T+166` | 10p | **CP5 (E1–E2) · Chỉ số & Event** | Viết 6–10 event có `trace_id` + kiểm tra chéo vào `chi_so.md` | Code & tính 3 chỉ số E1, điền bảng E1 & ≥ 2 rủi ro E2 vào `chi_so.md` | Đề xuất 1 chỉ số Dùng + 1 An toàn; rà ngôn ngữ (không viết "đã nâng") | Điền **Mục 4 & Mục 7** của `ho_so_launch_v0.md` | `report/team/chi_so.md` hoàn chỉnh |
| `16:46–16:56` | `T+166`–`T+176` | 10p | **CP5 (E3) · Chốt hồ sơ 1 trang** | Chạy `grep` kiểm tra từ cấm, check file | Đối chiếu lại toàn bộ số giữa 5 file | Audit toàn bộ C6–C8 (con số bất lợi, nhãn `simulated`, 1 vai trò) | Chốt **Đề xuất cuối** + điều kiện/người/ngày kiểm tra trong `ho_so_launch_v0.md` | `ho_so_launch_v0.md` sẵn sàng duyệt chéo |
| `16:56–17:00` | `T+176`–`T+180` | 4p | **CP5 · Chữa bài & Commit** | Chạy test tổng `lab13.py` | Xác nhận số khớp | Duyệt lần cuối | Push để gửi hồ sơ đúng **17:00** | Commit & push `feat(cp5)` |
| `17:00–17:10` | `T+180`–`T+190` | 10p | **Gate 2a · Trao đổi hồ sơ** | Kiểm tra hồ sơ nhóm `n + 1` đã nhận đủ | Đọc phần số liệu của nhóm `n + 1` | Đọc phần pilot & luật dừng của nhóm `n + 1` | Gửi hồ sơ nhóm mình cho nhóm hội đồng | Sẵn sàng chấm |
| `17:10–17:25` | `T+190`–`T+205` | 15p | **Gate 2a · Chấm nhóm `n + 1`** | Kiểm tra tính nhất quán số & `simulated` | Soát công thức & B4/D1 của nhóm bạn | Ghi điểm C6–C8, lý do có số, quyết định, 1 câu hỏi vào `phieu_cham.md` | Chuẩn bị pitch 1 phút cho hồ sơ nhóm mình | `report/team/phieu_cham.md` (trước phần Q&A) |
| `17:25–17:45` | `T+205`–`T+225` | 20p | **Gate 2a · Trình bày & Chốt** | Hỗ trợ trả lời kỹ thuật/event nếu được hỏi | Hỗ trợ trả lời số liệu nếu được hỏi | Ghi lại câu trả lời của đội bạn vào `phieu_cham.md` | Trình bày 1p + trả lời 1p trước hội đồng | Hoàn tất `phieu_cham.md` |
| `17:45–18:00` | `T+225`–`T+240` | 15p | **Đóng gói, Checklist & Push** | Chạy toàn bộ lệnh checklist & viết file cá nhân | Chạy `lab13.py` trên máy 2 & viết file cá nhân | Viết `group_report.md` & viết file cá nhân | Chốt `TEAM.md` & viết file cá nhân | Commit & push `docs(final)` |
| `18:00–23:59` | — | — | **Hậu kiểm & Nộp LMS** | Nộp link repo trên LMS | Nộp link repo trên LMS | Nộp link repo trên LMS | Kiểm tra repo public/đã mời GV; nhắc cả 4 nộp LMS | **4/4 thành viên nộp link trên LMS** |

---

## 5. Hướng dẫn kỹ thuật & Mốc số tự đối chiếu từng Checkpoint (CP1–CP5)

> Mọi hướng dẫn chi tiết và code mẫu tham khảo nằm trong [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Sai số cho phép so với số đối chiếu là **≤ 2%**. Mọi con số tính từ cột `phut_xem_lai_simulated` hoặc `phut_lam_lai_simulated` **bắt buộc ghi nhãn `simulated`**.

### CP1 · Nhiệm vụ A (`src/lab13.py` & `report/team/bang_chi_phi.md`)
- **Bắt buộc khi đọc CSV** (trong `src/`):
  ```python
  runs = pd.read_csv('logix_runs.csv')
  reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
  ```
  *(Thiếu `keep_default_na=False` sẽ biến ô trống ở `quyet_dinh_xem_lai` thành `NaN` và làm sai các phép lọc sau.)*
- **A1 — Ba phép thử bắt buộc (`p = 0,8`):** phải qua cả 3 và in `Ba phép thử đáp án biết trước: ĐẠT` mới được làm tiếp:
  - `so_lan_chay_ky_vong(0.8, 2)` = **`1,20`**
  - `so_lan_chay_ky_vong(0.8)` = **`1,25`**
  - `he_so_chi_phi_moi_viec_thanh_cong(0.8, 3)` = **`1,25`** (`= 1/p`, vì `k` triệt tiêu)
- **A2 — Mô hình chi phí từ trace:**
  - **Quy tắc cốt lõi:** tử số tính **MỌI lần chạy** (kể cả `status == 'loi'`); mẫu số chỉ đếm yêu cầu có `ket_qua == 'thanh_cong'`.
  - **Mốc đối chiếu:**
    - Token (mọi lần chạy): **`245.585 đ`** *(đo từ trace)*
    - Tool (5.600 lần gọi): **`84.000 đ`** *(đo từ trace)* · Trong đó lần chạy 2 & 3: **`93.804 đ`** *(đo từ trace)*
    - Xem lại (890 phút): **`1.780.000 đ`** `[simulated]` (**40,7%**)
    - Làm lại (1.132 phút): **`2.264.000 đ`** `[simulated]` (**51,8%** — khoản lớn nhất)
    - Tổng chi phí: **`4.373.585 đ`** *(có phần simulated)* · Số việc thành công: **`978`**
    - **Chi phí mỗi việc thành công (CPS):** **`4.472 đ`** `[simulated]`
    - Hoá đơn token + tool / số yêu cầu: **`274,7 đ`** *(đo từ trace)* → CPS thật gấp **`16,3 lần`** hoá đơn/yêu cầu.
  - **Lưu ý khi so với 12.000 đ:** KHÔNG lấy `4.472 / 12.000 = 0,37×` (vì 4.472 đ chưa tính phần nhân viên làm thay 222 yêu cầu không thành công). Phải tính chi phí cả hệ thống trên mỗi yêu cầu: `(4.373.585 + 222 × 12.000) / 1.200 =` **`5.865 đ/yêu cầu = 0,49×`** của 12.000 đ `[simulated]`.
- **A3 — Tách theo cột `loai`:**
  - `noi_dia` (824 yc · 95,0% thành công · 1,11 lần chạy): **`2.696 đ`** (**`0,22×`**) `[simulated]` → **Giữ trong pilot**.
  - `hang_nang` (158 yc · 74,1% · 1,47 lần chạy): **`8.221 đ`** (**`0,69×`**) `[simulated]` → **Giữ trong pilot**.
  - `quoc_te` (150 yc · 27,3% · 2,32 lần chạy): **`22.515 đ`** (**`1,88×`**) `[simulated]` → **Loại khỏi pilot**. Tỉ lệ ok theo lần thử giảm sâu (lần 1: 30% → lần 2: 11,4% → lần 3: 2,2%), chạy lại tới 3 lần không giúp.
  - `doi_tac` (68 yc · 54,4% · 1,88 lần chạy): **`10.215 đ`** (**`0,85×`**) `[simulated]` → **Loại khỏi pilot** (sát ngưỡng 12.000 đ và có điều khoản riêng).
- **A4 — Chi phí cố định 40 triệu đ/tháng (phạm vi `noi_dia` + `hang_nang`):**
  - Tỉ lệ thành công trong phạm vi trên mẫu: `900 / 1.200` (tổng chi phí biến đổi `3.072.513 đ` / `900` = `3.414 đ`).
  - Ở quy mô **45.000 yc/tháng**: `33.750` việc thành công/tháng → cố định **`+1.185 đ/việc`** → **`4.599 đ = 0,38×`** `[simulated]`.
  - Ở **một nửa khối lượng**: cố định **`+2.370 đ/việc`** → **`5.784 đ = 0,48×`** `[simulated]`.

### CP2 · Nhiệm vụ B (`src/lab13.py` & `report/team/bang_chi_phi.md`)
- **B1 — 9 kịch bản độ nhạy (tự kiểm tra: mức giảm của "giảm một nửa" = ½ mức tăng của "gấp đôi"):**
  - Token ×2: **`4.723 đ (+5,6%)`** · Token ÷2: **`4.346 đ (−2,8%)`**
  - Xem lại ×2: **`6.292 đ (+40,7%)`** · Xem lại ÷2: **`3.562 đ (−20,3%)`**
  - Làm lại ×2: **`6.787 đ (+51,8%)`** · Làm lại ÷2: **`3.315 đ (−25,9%)`**
  - Lương +25% (`2.500 đ/phút`): **`5.506 đ (+23,1%)`**
  - Tối đa 2 lần chạy: **`4.237 đ (−5,2%)`** · Chỉ 1 lần chạy: **`4.111 đ (−8,1%)`**
- **B2 — Đổi cặp & Xếp hạng:**
  - Token ×2 + Xem lại ×2 = **`6.543 đ (+46,3%)`** `[simulated]` (bằng đúng tổng 2 tác động riêng vì mô hình cộng tuyến tính).
  - **Top 3 yếu tố nhạy nhất:** **1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên**.
- **B3 — Chi phí cả hệ thống khi giới hạn số lần chạy (`tổng trợ lý + 12.000 × số không thành công`):**
  - Giới hạn 1 lần: trợ lý `3.621.781 đ`, `319` ca không thành công, cả hệ thống `7.449.781 đ`, CPS **`4.111 đ`** (thấp nhất).
  - Giới hạn **2 lần**: trợ lý `4.093.220 đ`, `234` ca không thành công, cả hệ thống **`6.901.220 đ` (rẻ nhất cho công ty)**, CPS `4.237 đ`.
  - Giới hạn 3 lần: trợ lý `4.373.585 đ`, `222` ca không thành công, cả hệ thống `7.037.585 đ`, CPS `4.472 đ`.
  - **Kết luận:** Giới hạn 2 lần rẻ nhất cho công ty; tối ưu riêng CPS (1 lần) đẩy thêm 85 ca sang nhân viên.
- **B4 — Xem lại 100% (`noi_dia` + `hang_nang`: 982 yêu cầu, 948 ca có ≥ 1 lần `status == 'ok'`, 48 ca `lam_lai`, token+tool `224.513 đ`, chia 900 việc thành công):**
  - **Bắt buộc ghi cả hai kịch bản phút làm lại:**
    - Giả định đề **9 phút/ca làm lại**: tổng `10.568.513 đ` → **`11.743 đ = 0,98×`** của 12.000 đ `[simulated]` (hòa vốn khi xem lại **≤ 5,1 phút/ca**).
    - Theo dữ liệu thực tế **`15,3` phút/ca** trung bình (trung vị 14,5): tổng `11.173.313 đ` → **`12.414 đ = 1,03×`** `[simulated]` — **đắt hơn nhân viên tự làm** (hòa vốn khi xem lại **≤ 4,8 phút/ca**).

### CP3 · Nhiệm vụ C (`report/team/bang_loi.md`) — Quy trình gắn nhãn liêm chính
- **Nguồn đề:** Mở mục *"Hai mươi ca lỗi"* trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
- **5 loại Google PAIR & Câu hỏi nhận diện nguyên nhân gốc:**
  1. **Do người dùng:** Đầu vào hoặc lựa chọn ban đầu của khách có sai không?
  2. **Hệ thống:** Trợ lý có làm sai so với thiết kế/chính sách và có người đã phát hiện ra không?
  3. **Ngữ cảnh:** Trợ lý làm đúng thiết kế nhưng giả định không khớp hoàn cảnh khiến khách thấy sai?
  4. **Giới hạn hệ thống:** Yêu cầu có nằm ngoài phạm vi, thiếu dữ liệu, hoặc không xử lý được dù cố gắng không?
  5. **Ngầm:** Có sai (về kết quả hoặc chi phí) nhưng cả khách lẫn hệ thống đều không nhận ra cho tới khi kiểm tra mẫu?
- **Quy tắc bắt buộc:**
  - **Gắn nhãn theo nguyên nhân gốc, KHÔNG theo chỗ cần sửa** (ví dụ: khách nhập sai mã và trợ lý không gợi ý sửa → vẫn là *Do người dùng*, phần gợi ý nằm ở cột khắc phục).
  - Phân biệt rõ **Hệ thống** (lỗi đã lộ ra) và **Ngầm** (không ai biết cho tới khi đối soát/kiểm tra mẫu).
  - **Liêm chính:** TV3 và TV4 ngồi tách nhau **8 phút**, tự gắn độc lập không trao đổi và **không dùng AI gắn thay**. Sau khi so, **không sửa lại 2 cột nhãn độc lập**; điền cột `Nhãn thống nhất` và viết 1 câu quy tắc phân biệt cho mỗi ca lệch. Đồng thuận mục tiêu **≥ 16/20 (80%)** (nếu < 80% phải viết lại định nghĩa trước khi qua bước 4).
  - **Bảng khắc phục 5 ca (mỗi loại 1 ca):** cột `Phát hiện bằng gì` phải **đo được** (tên event, ngưỡng cụ thể, tần suất); cột `Ai phụ trách` là **một vai trò cụ thể**, tuyệt đối không ghi `"cả đội"`.

### CP4 · Nhiệm vụ D (`src/lab13.py` & `report/team/pilot_plan.yaml`)
- **D1 — Cỡ mẫu (`baseline = 0,70`, mục tiêu `+5 điểm` → `0,75`, `alpha = 0,05`, `power = 0,80`, `ICC = 0,02`):**
  - a) Chia theo yêu cầu: **`1.251`** yêu cầu/nhóm *(1.250 nếu làm tròn z = 1,96 và 0,84)*.
  - b) Chia theo nhân viên, `m = 75`: `DE = 1 + 74 × 0,02 = 2,48` → cần **`3.103`** /nhóm → 42 người/nhóm (tổng `84 > 40` nhân viên hiện có: **không đủ người**).
  - c) 20 nhân viên/nhóm: trần `c / ICC = 20 / 0,02 =` tối đa **`1.000`** hiệu dụng `< 1.251` (**không đạt 5 điểm**).
  - d) 6 depot/nhóm: tối đa `6 / 0,02 =` **`300`** hiệu dụng và chỉ có `6 < 20` cụm (**loại**, dù dễ triển khai).
  - e) Nới MDE lên **6 điểm** (`0,76` → `859` hiệu dụng/nhóm) với **20 nhân viên/nhóm**: giải `20m / (1 + (m − 1) × 0,02) ≥ 859` → **`m ≥ 299`** yêu cầu/nhân viên (`DE = 6,96`).
- **Chọn cách chia & Đánh đổi minh bạch:**
  - Chọn **`unit: staff`** (20 nhân viên trợ lý vs 20 nhân viên đối chứng, phân tầng theo depot, gán ngẫu nhiên bằng seed cố định).
  - **Con số bất lợi bắt buộc nêu rõ:** chấp nhận **MDE = 6 điểm**; nếu tác động thật chỉ đạt 5 điểm thì **power giảm còn ~`0,64`** (tính bằng `NormalIndPower().power(...)`).
- **Tỉ lệ an toàn hiện tại trước khi viết luật dừng:**
  - `mo_lai_trong_7_ngay` hiện tại: **`4,25%`** (`51/1.200`) toàn mẫu; **`3,97%`** trong phạm vi `noi_dia` + `hang_nang`.
  - Vì nền đã ~4%, **KHÔNG đặt ngưỡng dừng 3%** (sẽ dừng ngay tuần đầu). Dùng ngưỡng so với đối chứng (ví dụ cao hơn đối chứng `≥ 2 điểm`) kèm trần tuyệt đối (ví dụ `> 6%`).
- **D2 & Trường bắt buộc trong `pilot_plan.yaml`:**
  - Ghi kết quả D1, 5 câu D2, đánh đổi và tỉ lệ mở lại vào phần `#` chú thích đầu file.
  - Điền sạch mọi dấu `?` ở các trường YAML (`owner`, `scope`, `assignment`, `n_per_arm`, `design_effect`, `clusters_per_arm`, `identifiability`, `stop_rules`, `rollback`, `decision_date`, `simulated_inputs`).
  - **3 luật dừng (An toàn, Chi phí, Mức độ sử dụng)** bắt buộc đủ 4 vế: **`NẾU`** `[chỉ số vượt ngưỡng]` **`TRONG`** `[thời hạn]` **`THÌ`** `[hành động + vai trò cụ thể]` **`KHÔNG THÌ`** `[việc bị cấm]`.

### CP5 · Nhiệm vụ E (`report/team/chi_so.md` & `report/team/ho_so_launch_v0.md`)
- **E1 — Tính thử 3 chỉ số trên 1.200 yêu cầu:**
  - Chính (`dong_trong_24h == 1 & mo_lai_trong_7_ngay == 0`): **`82,83%`** (`994/1.200`).
  - Dùng (tỉ lệ bỏ qua gợi ý `sua`/`bo` trên `duoc_xem_lai == 1`): **`27,12%`** (`48/177`).
  - An toàn (`mo_lai_trong_7_ngay == 1`): **`4,25%`** (`51/1.200`).
  - Tự đề xuất thêm **1 chỉ số Dùng** (ví dụ: % yêu cầu nhóm can thiệp có mở trợ lý) và **1 chỉ số An toàn** (ví dụ: % đơn sai tiền qua kiểm toán mẫu hằng tuần để bắt lỗi ngầm).
  - **Cảnh báo diễn đạt:** chỉ viết *"chỉ số trong đợt chạy thử là 82,83%"*; **tuyệt đối không viết** *"trợ lý đã nâng chỉ số"* (do chưa có nhóm đối chứng).
- **Danh sách Event & Kiểm tra chéo:**
  - Liệt kê **6–10 event**, mỗi event bắt buộc có `trace_id`, ghi rõ Ai tạo / Thuộc tính chính / Thời điểm.
  - Mục **Kiểm tra chéo:** ánh xạ từng chỉ số ở E1 dùng event nào để tính; nếu thiếu event thì ghi rõ là *chưa đo được*.
- **E2 — Rủi ro kinh tế:** tối thiểu **2–3 dòng** (làm lại ×2 → `6.787 đ`, `+51,8%`; xem lại 100% kéo dài → `11.743 đ = 0,98×` hoặc `12.414 đ = 1,03×`; khối lượng pilot giảm một nửa → cố định `+2.370 đ/việc`), ghi nhãn `simulated`, có dấu hiệu theo dõi, hành động, 1 vai trò phụ trách.
- **E3 — `ho_so_launch_v0.md`:**
  - Gói gọn **1 trang**, đủ **7 mục**. Cột Trạng thái chỉ dùng đúng 3 nhãn: **`Xong, có bằng chứng` · `Chưa` · `Giả lập`** (Mục 1, 2, 3, 7 ghi `Giả lập`).
  - Đề xuất cuối chọn 1 trong 3 (`Go` · `Go có điều kiện` · `No-go`). Nếu chọn **`Go có điều kiện`** cho pilot `noi_dia` + `hang_nang`, mỗi điều kiện phải gắn **vai trò phụ trách + ngày kiểm tra**, đồng thời công khai các con số bất lợi (power `0,64` ở 5 điểm, xem lại 100% có thể lên `1,03×`).

---

## 6. Quy ước Git & Phối hợp tránh Conflict cho nhóm 4 người

1. **Nguyên tắc Pull–Edit–Verify–Commit–Push:**
   - Luôn chạy `git pull --rebase origin main` trước khi bắt đầu phiên chỉnh sửa mới trên máy cá nhân.
   - Tuân thủ **Ma trận Single-Writer** ở Mục 3: không hai người cùng sửa một file Markdown/YAML ở cùng một checkpoint.
2. **Các mốc commit gợi ý trên nhánh `main`:**
   - `chore(setup): fill team roster and initial launch dossier shell`
   - `feat(cp1): implement A1-A4 cost model and fill bang_chi_phi part A`
   - `feat(cp2): add sensitivity scenarios B1-B4 and complete cost report`
   - `docs(cp3): add independent error labels, agreement and 5-case remediation`
   - `feat(cp4): add sample size D1 and complete pilot_plan.yaml`
   - `docs(cp5): complete chi_so.md and launch dossier v0 for Gate 2a`
   - `docs(final): add peer review scorecard, group report and member reports`
3. **Quy tắc liêm chính Git (theo `RULES.md`):**
   - **KHÔNG** `git push --force`, không xóa commit, không sửa ngày commit.
   - Nếu cần bổ sung sau 18:00 (nhưng trước 23:59 GMT+7), tạo commit mới và ghi rõ thay đổi.

---

## 7. Năm quy tắc sống còn, Chiến lược 30/30 điểm Hội đồng & Câu hỏi cần thuộc lòng

### 5 Quy tắc bắt buộc của Lab
1. Qua đủ **3 phép thử A1** (`1,20 · 1,25 · 1,25`) mới được làm tiếp.
2. Mọi con số tính từ hai cột `_simulated` phải ghi nhãn **`simulated`**.
3. Đối chiếu ngay khi slide chữa hiện lên (nhiệm vụ sau dùng lại số của nhiệm vụ trước).
4. Mỗi câu trả lời trong báo cáo **không quá 3 dòng**, có **ít nhất 1 con số**.
5. **KHÔNG dùng từ "production"** trong bất kỳ file hồ sơ nào: Gate 2a chỉ duyệt kế hoạch pilot.

### 10 lỗi hay mất điểm nhất cần tránh
1. Quên `keep_default_na=False` khi đọc `logix_requests.csv`.
2. Tính CPS chỉ lấy token của lần chạy thành công, hoặc chia cho 1.200 thay vì 978, hoặc quên chia 1.000 token.
3. So sánh `4.472 / 12.000 = 0,37×` mà quên phần nhân viên làm thay 222 ca lỗi (đúng phải là **`0,49×`**).
4. Thiếu nhãn `simulated` trên bảng A2, A3, A4, B1–B4, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`.
5. Ghi người phụ trách là `"cả đội"` thay vì một vai trò cụ thể có quyền quyết định.
6. B4 chỉ báo cáo `11.743 đ (0,98×)` mà bỏ quên độ nhạy **`15,3` phút làm lại** cho ra **`12.414 đ (1,03×)`**.
7. Gắn nhãn lỗi sau khi trao đổi, hoặc sửa lại cột nhãn gốc sau khi so.
8. Chọn chia pilot theo depot (`6 + 6`) vì dễ triển khai dù chỉ có 6 cụm (`< 20`) và tối đa 300 hiệu dụng.
9. Đặt ngưỡng an toàn 3% khi tỉ lệ mở lại hiện tại đã là `4,25%` (`3,97%` trong phạm vi).
10. Viết trợ lý *"đã nâng"* chỉ số trong khi đợt chạy thử không có đối chứng.

### Chiến lược đạt trọn 30/30 điểm Hội đồng (C6–C8)
- **C6 (10đ — Đề xuất khớp bằng chứng):** Chủ động đưa con số bất lợi lên ngay cạnh đề xuất (ví dụ: *power chỉ còn `0,64` ở mức 5 điểm*; *xem lại 100% với làm lại `15,3` phút sẽ tốn `1,03×` so với tự làm*; *tỉ lệ mở lại hiện là `3,97%`–`4,25%`*) kèm điều kiện xử lý cụ thể (người phụ trách + ngày kiểm tra). Một đề xuất thận trọng khớp số luôn thắng đề xuất lạc quan bỏ qua số bất lợi.
- **C7 (10đ — Số giả lập & phạm vi):** Gắn nhãn `simulated` nhất quán ở tất cả số phát sinh từ giờ xem lại/làm lại; nêu rõ phạm vi pilot chỉ gồm **`noi_dia` (`0,22×`) + `hang_nang` (`0,69×`)**, loại **`quoc_te` (`1,88×`, thành công `27,3%`)** và **`doi_tac` (`0,85×`, điều khoản riêng)**.
- **C8 (10đ — Pilot ra được quyết định):** Đối chứng song song 20+20 nhân viên phân tầng theo depot, ghi rõ seed ngẫu nhiên trước khi chạy, đủ 3 luật dừng có ngưỡng định lượng + thời hạn + người có quyền bấm tắt trong 30 phút.

### 3 câu hỏi cốt lõi cả 4 thành viên phải tự giải thích được (nếu GV/Hội đồng hỏi)
1. **Vì sao tử số tính mọi lần chạy kể cả lần lỗi, còn mẫu số chỉ đếm `ket_qua == 'thanh_cong'`?**  
   → Vì mỗi lần chạy lỗi vẫn tiêu tốn token, tool và thời gian xử lý/làm lại; nhưng kết quả kinh doanh nhận được chỉ là những yêu cầu thực sự giải quyết xong (`thanh_cong`). Nếu bỏ lần lỗi khỏi tử số hoặc chia cho tổng số yêu cầu sẽ làm chi phí bị đánh giá thấp giả tạo.
2. **Vì sao chia theo cụm làm giảm cỡ mẫu hiệu dụng (`n_hiệu_dụng = c × m / DE < c / ICC`) và vì sao nhóm chọn 20+20 nhân viên?**  
   → Các yêu cầu do cùng một nhân viên/depot xử lý có tương quan nội cụm (`ICC = 0,02`), làm giảm thông tin độc lập theo hệ số thiết kế `DE = 1 + (m − 1) × ICC`. Với `c` cụm, dù tăng `m` lên vô cực thì `n_hiệu_dụng` vẫn bị chặn trên bởi `c / ICC` (`6 depot → tối đa 300`; `20 nhân viên → tối đa 1.000 < 1.251` nên phải chấp nhận MDE `6 điểm`, `n = 859`, `m ≥ 299`).
3. **Vì sao nhóm đưa ra đề xuất cuối (ví dụ `Go có điều kiện`) và chấp nhận những con số bất lợi nào?**  
   → Trong phạm vi thu hẹp `noi_dia + hang_nang`, chi phí đạt `0,38×` ở quy mô 45.000 yc/tháng (`simulated`), nhưng chỉ giữ được lợi thế kinh tế khi kiểm soát được tỉ lệ làm lại và giảm dần xem lại xuống dưới mức hòa vốn `4,8–5,1` phút/ca; đồng thời phải bù khuyết kỹ thuật trước khi bấm nút pilot.

---

## 8. Checklist tự kiểm tra & Lệnh xác minh trước khi nộp

### Lệnh chạy xác minh (tại thư mục gốc repo hoặc `src/`)
```bash
# 1. Chạy toàn bộ pipeline trên ít nhất 2 máy khác nhau (TV1 & TV2)
cd src && python3 lab13.py

# 2. Kiểm tra YAML đọc được hợp lệ và không còn dấu '?' ngoài dòng chú thích
cd .. && python3 -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"
grep -v '^ *#' report/team/pilot_plan.yaml | grep -n '?' || echo "OK: khong con dau hoi"

# 3. Kiểm tra không có từ cấm trong hồ sơ và không ghi 'cả đội'
grep -rni "production" report/team/ || echo "OK: khong co tu cam"
grep -rni "cả đội" report/team/ || echo "OK: khong co 'ca doi'"

# 4. Kiểm tra sạch file gốc và không lọt .venv / .env
git status
```

### Checklist hành chính trước 18:00 & 23:59 GMT+7
- [ ] Tên repo đúng chuẩn `K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` (public hoặc đã mời giảng viên).
- [ ] `TEAM.md` ở root điền đủ thông tin nhóm, 4 thành viên, vai trò (có đổi vai viết code), đóng góp & bằng chứng.
- [ ] Đủ **6 file hồ sơ** trong `report/team/` đúng tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`.
- [ ] Có `report/team/group_report.md` (≤ 2 trang).
- [ ] Có đủ **4 file báo cáo cá nhân** `report/team/<MSSV>_<HoTen>.md` và giữ nguyên file mẫu `report/team/MSSV_HoTen.md`.
- [ ] `cd src && python3 lab13.py` chạy hết trên máy khác trong nhóm, 3 phép thử A1 in `ĐẠT`.
- [ ] Mọi số từ cột `_simulated` có nhãn `simulated`; mọi câu trả lời ≤ 3 dòng và có số.
- [ ] Đề xuất cuối trong `ho_so_launch_v0.md` là một trong ba: `Go`, `Go có điều kiện`, `No-go`.
- [ ] Không sửa `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`; không commit `.venv/`, `.env`.
- [ ] **Cả 4 thành viên đều đã tự nộp cùng link repo nhóm trên LMS trước 23:59 GMT+7.**
