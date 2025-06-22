# 🛍️ Hệ Thống Đề Xuất Sản Phẩm Thương Mại Điện Tử

## 📌 Giới thiệu

Hệ thống đề xuất sản phẩm thông minh kết hợp nhiều phương pháp để đưa ra gợi ý chính xác cho người dùng. Hệ thống tích hợp:

- Đề xuất theo người dùng đơn lẻ: Phân tích hành vi và sở thích cá nhân
- Đề xuất cho nhiều người dùng: Xử lý hàng loạt người dùng đồng thời
- Phân tích cảm xúc: Đánh giá cảm xúc từ đánh giá sản phẩm

---

## 📚 Mục lục

- [✨ Tính năng chính](#-tính-năng-chính)
- [🛠️ Công nghệ sử dụng](#️-công-nghệ-sử-dụng)
- [📦 Cài đặt](#-cài-đặt)
- [🤖 Tải mô hình phân tích cảm xúc](#-tải-mô-hình-phân-tích-cảm-xúc)
- [📁 Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [📊 Công thức tính điểm Hybrid](#-công-thức-tính-điểm-hybrid)
- [🚀 Cách sử dụng](#-cách-sử-dụng)
- [📬 Liên hệ & đóng góp](#-liên-hệ--đóng-góp)

---

## ✨ Tính năng chính

### 1. Hệ thống đề xuất Hybrid
- Kết hợp Content-based và Collaborative Filtering
- Tích hợp thông tin người dùng, sản phẩm và cảm xúc
- Gợi ý theo ngữ cảnh và hành vi thực tế

### 2. Phân tích cảm xúc
- Hỗ trợ đa ngôn ngữ:
  - ✅ Tiếng Anh: BERT-base
  - ✅ Tiếng Việt: PhoBERT
- Tự động phát hiện ngôn ngữ
- Phân tích đánh giá theo thời gian thực
- Giao diện trực quan, dễ sử dụng

### 3. Xử lý dữ liệu
- Nhập liệu đa dạng (CSV, nhập trực tiếp)
- Tự động phát hiện ngôn ngữ
- Xử lý dữ liệu quy mô lớn

---

## 🛠️ Công nghệ sử dụng

| Ngôn ngữ / Thư viện       | Mô tả                                                                 |
|---------------------------|----------------------------------------------------------------------|
| **Python 3.8+**            | Ngôn ngữ lập trình chính                                             |
| **BERT / PhoBERT**         | Phân tích cảm xúc tiếng Anh & tiếng Việt                             |
| **Scikit-learn, Surprise** | Xây dựng mô hình đề xuất sản phẩm                                   |
| **Torch, Transformers**    | Triển khai mô hình học sâu NLP                                      |
| **Streamlit**              | Tạo giao diện người dùng trực quan                                  |
| **Huggingface Hub**        | Tải mô hình pretrained từ Hugging Face                              |

---

## 📦 Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/buiductai13/Sentiment_Analysis_System-.git
cd Sentiment_Analysis_System-

### 2. Tạo môi trường ảo & kích hoạt
🔹 Trên Windows:

bash

python -m venv venv
venv\Scripts\activate
🔹 Trên macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Cài đặt thư viện phụ thuộc
bash
Copy code
pip install -r requirements.txt
🤖 Tải mô hình phân tích cảm xúc
Hệ thống sử dụng các mô hình có sẵn trên Hugging Face:

🔹 Mô hình tiếng Anh (BERT-base)
python
Copy code
from huggingface_hub import snapshot_download
snapshot_download(repo_id='buiductai/Analyze_user_sentiment_through_comments_ENG', local_dir='model/english_sentiment')
🔗 Xem mô hình

🔹 Mô hình tiếng Việt (PhoBERT)
python
Copy code
from huggingface_hub import snapshot_download
snapshot_download(repo_id='buiductai/Analyze_user_sentiment_through_comments_VN', local_dir='model/vietnamese_sentiment')
🔗 Xem mô hình

📁 Cấu trúc thư mục
plaintext
Copy code
Sentiment_Analysis_System-/
├── app_vn.py               # Ứng dụng chính phân tích cảm xúc tiếng Việt
├── data/                   # Dữ liệu đầu vào (bị ignore khi push GitHub)
├── model/                  # Các mô hình đã huấn luyện (bị ignore)
├── src/                    # Mã nguồn chính
│   ├── recommender.py      # Mô hình đề xuất sản phẩm
│   └── sentiment.py        # Mô hình phân tích cảm xúc
├── danhgia_phim_vn.xlsx    # Dataset tiếng Việt
├── movie_reviews_en.xlsx   # Dataset tiếng Anh
├── requirements.txt        # Thư viện cần cài
└── Readme.md               # Mô tả dự án
📊 Công thức tính điểm Hybrid
python
Copy code
hybrid_score = (w1 * svd_score) + (w2 * content_similarity) + (w3 * price_similarity) + (w4 * user_sentiment)
Trọng số có thể chỉnh trong settings.py:

python
Copy code
HYBRID_SCORE_WEIGHTS = {
    'svd_score': 0.2,
    'content_similarity': 0.3,
    'price_similarity': 0.3,
    'user_sentiment': 0.2
}
🚀 Cách sử dụng
bash
Copy code
streamlit run app_vn.py
📬 Liên hệ & Đóng góp
📧 Email: buiductaicntt@gmail.com

🌐 GitHub: github.com/buiductai13

💼 LinkedIn: linkedin.com/in/taibuiduc1303

