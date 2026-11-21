# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | 5.600 lượt gọi trong `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 (token + tool) | 93.804 | `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 | 890 phút từ `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | 1.132 phút từ `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ CSV |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí chia 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | Token + tool chia 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn token và tool trên mỗi yêu cầu (`simulated`).
- Làm lại là khoản lớn nhất, **2.264.000 đ**, chiếm **51,8%** tổng chi phí (`simulated`).
- Cộng chi phí nhân viên xử lý 222 yêu cầu chưa thành công, cả hệ thống tốn **5.865 đ/yêu cầu**, bằng **0,49×** mức 12.000 đ (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- `quoc_te` tốn **1,88×** mức nhân viên tự làm (`simulated`). Tỷ lệ `ok` giảm từ **30,0%** xuống **11,4%** rồi **2,2%** qua ba lần thử, nên lợi ích của lần chạy thêm rất thấp.
- `doi_tac` sát ngưỡng (**0,85×**, thành công 54,4%, `simulated`) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot; pilot chỉ giữ `noi_dia` + `hang_nang`.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Với 40 triệu đ cố định mỗi tháng, chi phí vẫn dưới 12.000 đ ở cả hai mức. Khi khối lượng giảm một nửa, chi phí tăng từ **4.599 đ** lên **5.784 đ/việc thành công** (`simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giữ nguyên giá tool | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có `attempt > 2`, chuyển yêu cầu có `so_lan_chay > 2` cho nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Cùng cách tính với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi cho **6.543 đ/việc thành công (+46,3%)** (`simulated`). Mức tăng bằng tổng hai thay đổi riêng trên cùng mẫu số.
- Ba yếu tố nhạy nhất theo kịch bản đã thử là **số ca làm lại (+51,8%)**, **tỉ lệ xem lại (+40,7%)** và **lương nhân viên (+23,1%)** (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **2 lần** rẻ nhất cho công ty (**6.901.220 đ**). Giới hạn **1 lần** cho chi phí mỗi việc thành công thấp nhất (**4.111 đ**) nhưng thêm **85** yêu cầu cần nhân viên xử lý (`simulated` cho các khoản chi phí).

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% gợi ý trong `noi_dia` + `hang_nang` tốn **11.743 đ (0,98×)** nếu làm lại mất 9 phút/ca, hoặc **12.415 đ (1,03×)** nếu dùng trung bình chưa làm tròn từ CSV (xấp xỉ 15,30 phút/ca). Cả hai kết quả đều là `simulated`.
- Pilot cần đo phút xem lại và phút làm lại. Ngưỡng xem lại hòa vốn lần lượt là **5,1** và **4,8 phút/ca** (`simulated`).
