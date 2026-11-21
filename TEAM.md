# Team

## Thông tin nhóm

- Tên nhóm: `QuanHocOnline`
- Lớp: `L3A`
- Repo nhóm: `K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/Khoaitay51/K5-L3A-DAY13-QuanHocOnline-LaunchEconomics` · nhánh `main` · *(cập nhật commit chốt cuối buổi)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Trường Chinh | 2A202603426 | phemchinh1708@gmail.com | Khoaitay51 | Người viết code (CP1–CP2) → Kỹ sư kiểm chứng & Event (CP3–CP5) |
|   2 | Nguyễn Minh Quân | 2A202603510 | | | Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5) |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## PhamTruongChinh-2A202603426

### Phần việc phụ trách

- Cài đặt môi trường Python (`.venv`), lập trình `src/lab13.py` cho CP1 (A1–A4) và CP2 (B1–B4), bàn giao code cho TV2 sau giờ giải lao.
- Thiết kế danh sách 10 event có `trace_id` và ánh xạ kiểm tra chéo trong `report/team/chi_so.md`.
- Lập kế hoạch phân việc & timeline 4 người (`IMPLEMENTATION_PLAN.md`), thực hiện kiểm tra kỹ thuật YAML/checklist cuối buổi.

### Đóng góp cụ thể

- Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Viết `mo_hinh(...)` và các bảng tính A2–A4, độ nhạy B1–B4 trên dữ liệu giả lập (gắn nhãn `simulated` đầy đủ).
- Hoàn thiện phần Danh sách event (10 event có `trace_id`) và Kiểm tra chéo event ↔ chỉ số trong `report/team/chi_so.md`.

### Bằng chứng

- `src/lab13.py`, `report/team/chi_so.md` (phần Danh sách event & Kiểm tra chéo), `report/team/2A202603426_PhamTruongChinh.md`, `IMPLEMENTATION_PLAN.md`.

## NguyenMinhQuan-2A202603510

### Phần việc phụ trách

- Kiểm số và điền bảng chi phí A1–A4, B1–B4.
- Tiếp quản `src/lab13.py` để tính cỡ mẫu pilot D1 và ba chỉ số E1. Ghi số liệu D1 trong kế hoạch pilot và lập bảng rủi ro kinh tế E2.

### Đóng góp cụ thể

- Đối chiếu chi phí theo giới hạn số lần chạy. Hai lần chạy cho chi phí toàn hệ thống thấp nhất là 6.901.220 đ (`simulated`).
- Tính phương án 20 nhân viên mỗi nhóm, tối thiểu 299 yêu cầu mỗi người để phát hiện chênh lệch 6 điểm phần trăm, và power 64,17% nếu tác động thực chỉ đạt 5 điểm.
- Tính các tỷ lệ quan sát E1 là 82,83%, 27,12% và 4,25%. Ghi ba rủi ro kinh tế về làm lại, xem lại và khối lượng.

### Bằng chứng

- `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` (D1), `report/team/chi_so.md` (số E1 và bảng E2), `report/team/2A202603510_NguyenMinhQuan.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
