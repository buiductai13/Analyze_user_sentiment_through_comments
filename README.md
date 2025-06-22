## 🧠 Sentiment Analysis & Recommendation System for E-Commerce

## 🚀 Giới thiệu

Đây là một hệ thống thông minh giúp **phân tích cảm xúc của người dùng** và **đưa ra đề xuất sản phẩm phù hợp** trong lĩnh vực thương mại điện tử. Dự án được xây dựng với mục tiêu:

- Tích hợp phân tích cảm xúc đa ngôn ngữ (Tiếng Việt & Tiếng Anh)
- Kết hợp mô hình đề xuất dựa trên hành vi người dùng và nội dung sản phẩm
- Xử lý dữ liệu lớn, hỗ trợ giao diện tương tác người dùng dễ dùng

> 🔎 **Ứng dụng công nghệ AI hiện đại trong xử lý ngôn ngữ tự nhiên và đề xuất sản phẩm**  
> 🧪 Dự án liên quan trực tiếp tới các nội dung đã thực hiện tại kỳ thực tập và cuộc thi khoa học dữ liệu đại học (theo CV).

## ✨ Tính năng chính

- ✅ Phân tích cảm xúc người dùng theo thời gian thực
- ✅ Hỗ trợ ngôn ngữ tiếng Việt (PhoBERT) và tiếng Anh (BERT)
- ✅ Tự động phát hiện ngôn ngữ trong văn bản đánh giá
- ✅ Hệ thống đề xuất sản phẩm kết hợp (hybrid) sử dụng:
  - SVD (Collaborative Filtering)
  - Content-based Filtering
  - Cảm xúc người dùng (Sentiment score)
- ✅ Giao diện người dùng đơn giản bằng Streamlit

## 📂 Cấu trúc thư mục dự án

Sentiment_Analysis_System-/
├── data/
├── model/
├── src/
├── app_vn.py
├── danhgia_phim_vn.xlsx
├── movie_reviews_en.xlsx
└── Readme.md

## 🛠️ Công nghệ sử dụng
Công nghệ	Mô tả
Python 3.8+	Ngôn ngữ lập trình chính
BERT / PhoBERT	Phân tích cảm xúc tiếng Anh & Việt
Scikit-learn, Surprise	Xây dựng mô hình đề xuất sản phẩm
Torch, Transformers	Mô hình NLP sâu
Streamlit	Tạo giao diện người dùng trực quan
Huggingface Hub	Tải mô hình pretrained

📦 Hướng dẫn cài đặt
1. Clone dự án
_ git clone https://github.com/buiductai13/Sentiment_Analysis_System-.git
- cd Sentiment_Analysis_System-

2. Tạo và kích hoạt môi trường ảo
🔹 Trên Windows:
python -m venv venv
venv\Scripts\activate
🔹 Trên macOS/Linux:
python3 -m venv venv
source venv/bin/activate
3. Cài đặt thư viện phụ thuộc
pip install -r requirements.txt

🤖 Tải mô hình phân tích cảm xúc

Mô hình tiếng Anh (BERT):
- python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='buiductai/Analyze_user_sentiment_through_comments_ENG', local_dir='model/english_sentiment')"
Mô hình tiếng Việt (PhoBERT):
- python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='buiductai/Analyze_user_sentiment_through_comments_VN', local_dir='model/vietnamese_sentiment')"


🚀 Chạy ứng dụng

streamlit run app_vn.py
📊 Công thức tính điểm đề xuất Hybrid

hybrid_score = (w1 * svd_score) + (w2 * content_similarity) + (w3 * price_similarity) + (w4 * user_sentiment)

Các trọng số có thể chỉnh trong settings.py:

HYBRID_SCORE_WEIGHTS = {
    'svd_score': 0.2,
    'content_similarity': 0.3,
    'price_similarity': 0.3,
    'user_sentiment': 0.2
}

📬 Liên hệ và đóng góp:
📧 Email: buiductaicntt@gmail.com

🌐 GitHub: github.com/buiductai13

💼 LinkedIn: linkedin.com/in/taibuiduc1303

🏆 Thành tích liên quan:

✅ Xây dựng hệ thống phân tích cảm xúc và đề xuất sản phẩm cho các cuộc thi khoa học dữ liệu tại đại học

✅ Áp dụng thực tiễn vào mô hình học sâu (Deep Learning), NLP và ứng dụng web thực tế

✅ Đạt kết quả F1-score 0.88 và xử lý hơn 10.000 bản ghi dữ liệu người dùng
