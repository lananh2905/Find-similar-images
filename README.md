<h1 align="center"><b>FIND SIMILAR IMGAES</b></h1>

## Thông tin project

* **Mục đích:** Tải lên 1 ảnh bất kì từ tập seg_test của dataset, dùng đặc trưng `Histogram` và độ đo `Euclidean` để tìm ra 10 ảnh giống với ảnh trên nhất trong tập seg của dataset.
* **Input:** 1 ảnh trong tập seg_test.
* **Output:** 10 ảnh trong tập seg giống với ảnh input nhất.
* **Công cụ sữ dụng:** VS code
* **Ngôn ngữ:** `python`, `html`, `css`

## Setup

* **Install các thư viện của python:** cv2, os, pandas, numpy, flask, scipy
```bash
pip install opencv-python, os, pandas, numpy, flask, scipy
```

* **Dataset:** thêm dataset vào thư mục `static/dataset`

* **Rút trích đặc trưng từ dataset:**
```bash
python extract_features.py
```

* **Chạy chương trình bằng lệnh:**
```bash
python app.py
```

* **Truy cập đường link để nhìn thấy trang web:**
```bash
http://127.0.0.1:5000/
```
## Công dụng các hàm

|  Tên File, Folder | Description |
|---|---|
| `app.py` | Tệp chính để thực hiện tìm kiếm 10 ảnh giống nhất, chuyển hướng kết quả đến file `index.html` |
| `extract_features.py` | Rút trích đặc trưng histogram từ folder `seg_test`, lưu link ảnh từ folder `seg`, `seg_test` để file index.html dễ dàng truy xuất đến ảnh khi tìm thấy. Lưu tất cả vào folder `database` |
| `image_search` | Chứa hàm dùng để rút trích đặc trưng ảnh |
| `database` | Chứa đặc trưng `histogram` của ảnh trong folder `seg`, link ảnh từ folder `seg`, `seg_test` |
| `templates` | Chứa file `index.html` dùng để hiển thị trang web |
| `static` | Chứa folder `dataset` chứa anh, file `style.css` để làm đẹp trang web |

## Hiển thị
![image](https://github.com/user-attachments/assets/7932d771-c0d8-4a88-bb80-adaac333e1b8)

## Create by

* **Github:** [lananh2905](https://github.com/lananh2905)
* **Email:** 22520083@gm.uit.edu.vn


<!-- Footer -->
<p align='center'>Copyright © 2024 - Trịnh Thị Lan Anh</p>
