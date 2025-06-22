# 🧠 Sentiment Analysis & Recommendation System for E-Commerce

## 🚀 Giới thiệu

Đây là một hệ thống thông minh giúp **phân tích cảm xúc của người dùng** và **đề xuất sản phẩm phù hợp** trong lĩnh vực thương mại điện tử. Dự án được xây dựng với mục tiêu:

- Tích hợp phân tích cảm xúc đa ngôn ngữ (Tiếng Việt & Tiếng Anh)
- Kết hợp mô hình đề xuất dựa trên hành vi người dùng và nội dung sản phẩm
- Xử lý dữ liệu lớn, hỗ trợ giao diện tương tác người dùng dễ dùng

> 🔎 Ứng dụng công nghệ AI hiện đại trong xử lý ngôn ngữ tự nhiên và đề xuất sản phẩm  
> 🧪 Dự án liên quan trực tiếp tới kỳ thực tập và các cuộc thi khoa học dữ liệu đại học

---

## ✨ Tính năng chính

- ✅ Phân tích cảm xúc người dùng theo thời gian thực
- ✅ Hỗ trợ ngôn ngữ tiếng Việt (PhoBERT) và tiếng Anh (BERT)
- ✅ Tự động phát hiện ngôn ngữ trong văn bản đánh giá
- ✅ Hệ thống đề xuất sản phẩm kết hợp (Hybrid) sử dụng:
  - SVD (Collaborative Filtering)
  - Content-based Filtering
  - Sentiment Score (điểm cảm xúc)
- ✅ Giao diện người dùng đơn giản với Streamlit

---

## 📁 Cấu trúc thư mục

```plaintext
Sentiment_Analysis_System-/
├── app_vn.py               # Ứng dụng chính phân tích cảm xúc tiếng Việt
├── data/                   # Dữ liệu đầu vào (được ignore khi push GitHub)
├── model/                  # Các mô hình đã huấn luyện (được ignore)
├── src/                    # Source code chính của hệ thống
│   ├── recommender.py      # Mô hình đề xuất sản phẩm
│   └── sentiment.py        # Bộ phân tích cảm xúc
├── danhgia_phim_vn.xlsx    # Dataset đánh giá phim tiếng Việt
├── movie_reviews_en.xlsx   # Dataset đánh giá phim tiếng Anh
├── requirements.txt        # Thư viện phụ thuộc
└── Readme.md               # File mô tả dự án
