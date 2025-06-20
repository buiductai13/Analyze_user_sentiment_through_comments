import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import os
from datetime import datetime
import plotly.express as px

# Tải mô hình và tokenizer
@st.cache_resource
def load_models():
    en_model_path = 'model/save_model'
    en_model = AutoModelForSequenceClassification.from_pretrained(en_model_path)
    en_tokenizer = AutoTokenizer.from_pretrained(en_model_path)

    vn_model_path = 'model/save_model_vn'
    vn_model = AutoModelForSequenceClassification.from_pretrained(vn_model_path)
    vn_tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")

    return (en_model, en_tokenizer), (vn_model, vn_tokenizer)

(en_model, en_tokenizer), (vn_model, vn_tokenizer) = load_models()

# Ánh xạ nhãn
en_label_dict = {0: 'Positive', 1: 'Negative', 2: 'Neutral', 3: 'Irrelevant'}
vn_label_dict = {0: 'Tiêu cực', 1: 'Tích cực'}

# Hàm dự đoán cảm xúc
def predict_sentiment(text, model, tokenizer, label_dict, device):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    
    return label_dict[predicted_class]

# Hàm lưu lịch sử vào file CSV
def save_history(history_df):
    if os.path.exists('sentiment_history.csv'):
        history_df.to_csv('sentiment_history.csv', mode='a', header=False, index=False)
    else:
        history_df.to_csv('sentiment_history.csv', mode='w', header=True, index=False)

# Tải lịch sử từ file CSV
def load_history():
    if os.path.exists('sentiment_history.csv'):
        return pd.read_csv('sentiment_history.csv')
    else:
        return pd.DataFrame(columns=['Text', 'Sentiment', 'Timestamp', 'Language'])

# Tiêu đề đề tài
st.title('Phân tích trạng thái bằng mô hình BERT')

# Tạo tab
tab1, tab2, tab3 = st.tabs(["Phân tích văn bản đầu vào", "Phân tích đa văn bản đầu vào", "Phân tích file CSV"])

# Hàm chung để chọn ngôn ngữ
def language_selector(key):
    return st.radio("Chọn ngôn ngữ:", ["Tiếng Anh", "Tiếng Việt"], key=key)

# Tab 1: Phân tích một đoạn văn bản
with tab1:
    st.header("Phân tích trạng thái văn bản")
    # language = language_selector()
    language = language_selector("lang_selector_tab1")
    text_input = st.text_area("Điền nội dung của bạn vào đây:", height=100)
    if st.button('Phân tích trạng thái', key='single'):
        if text_input:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            if language == "Tiếng Anh":
                sentiment = predict_sentiment(text_input, en_model, en_tokenizer, en_label_dict, device)
            else:
                sentiment = predict_sentiment(text_input, vn_model, vn_tokenizer, vn_label_dict, device)
            st.write(f"Trạng thái của nội dung này là: **{sentiment}**")
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_history(pd.DataFrame([{'Text': text_input, 'Sentiment': sentiment, 'Timestamp': timestamp, 'Language': language}]))
        else:
            st.warning("Vui lòng điền nội dung vào.")

# Tab 2: Phân tích nhiều đoạn văn bản (nhập thủ công)
with tab2:
    st.header("Phân tích trạng thái đa văn bản")
    # language = language_selector()
    language = language_selector("lang_selector_tab2")
    num_texts = st.number_input("Số lượng nội dung muốn phân tích", min_value=1, max_value=10, value=3)
    texts = []
    for i in range(num_texts):
        text = st.text_area(f"Nội dung số {i+1}", height=100, key=f"text_{i}")
        texts.append(text)
    
    if st.button('Phân tích trạng thái', key='multiple'):
        results = []
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        for i, text in enumerate(texts):
            if text:
                if language == "Tiếng Anh":
                    sentiment = predict_sentiment(text, en_model, en_tokenizer, en_label_dict, device)
                else:
                    sentiment = predict_sentiment(text, vn_model, vn_tokenizer, vn_label_dict, device)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results.append({"Text": text, "Sentiment": sentiment, "Timestamp": timestamp, "Language": language})
            else:
                st.warning(f"Nội dung số {i+1} trống nên sẽ bỏ qua.")
        
        if results:
            df_results = pd.DataFrame(results)
            st.write(df_results)
            save_history(df_results)

            # Tạo biểu đồ tròn phân phối cảm xúc sử dụng Plotly
            sentiment_counts = df_results['Sentiment'].value_counts().reset_index()
            sentiment_counts.columns = ['Sentiment', 'Count']
            fig = px.pie(sentiment_counts, values='Count', names='Sentiment', 
                        title='Phân phối trạng thái',
                        color='Sentiment',
                        color_discrete_map={'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#bdc3c7', 'Irrelevant': 'black',
                                            'Tích cực': '#2ecc71', 'Tiêu cực': '#e74c3c'})
            st.plotly_chart(fig)
        else:
            st.warning("Không có nội dung nào hợp lệ để phân tích.")

# Tab 3: Phân tích nhiều đoạn văn bản từ file CSV
with tab3:
    st.header("Phân tích trạng thái từ file CSV")
    language = language_selector("lang_selector_tab3")
    uploaded_file = st.file_uploader("Chọn file CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Xem trước 5 dòng đầu tiên của file CSV:")
        st.write(df.head())
        
        # Cho phép người dùng chọn cột để phân tích
        column_to_analyze = st.selectbox("Chọn cột để phân tích:", df.columns)
        
        # Thêm tùy chọn chọn cột chủ đề
        topic_column = st.selectbox("Chọn cột phân tích theo chủ đề (không bắt buộc):", ["Không chọn"] + list(df.columns))
        
        if st.button('Phân tích trạng thái', key='csv'):
            with st.spinner('Đang phân tích ...'):
                device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
                if language == "Tiếng Anh":
                    df['sentiment'] = df[column_to_analyze].astype(str).apply(lambda x: predict_sentiment(x, en_model, en_tokenizer, en_label_dict, device))
                else:
                    df['sentiment'] = df[column_to_analyze].astype(str).apply(lambda x: predict_sentiment(x, vn_model, vn_tokenizer, vn_label_dict, device))
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                df['timestamp'] = timestamp
                df['language'] = language
                st.write(df)
                st.success('Phân tích hoàn tất!')
                save_history(df[[column_to_analyze, 'sentiment', 'timestamp', 'language']].rename(columns={column_to_analyze: 'Text', 'sentiment': 'Sentiment', 'timestamp': 'Timestamp', 'language': 'Language'}))
            
            # Tạo biểu đồ tròn phân phối cảm xúc tổng thể
            st.subheader("Phân phối trạng thái tổng thể")
            sentiment_counts = df['sentiment'].value_counts().reset_index()
            sentiment_counts.columns = ['Sentiment', 'Count']
            fig = px.pie(sentiment_counts, values='Count', names='Sentiment', 
                        title='Phân phối trạng thái tổng thể',
                        color='Sentiment',
                        color_discrete_map={'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#bdc3c7', 'Irrelevant': 'black',
                                            'Tích cực': '#2ecc71', 'Tiêu cực': '#e74c3c'})
            st.plotly_chart(fig)
            
            # Nếu có chọn cột chủ đề, phân tích theo từng chủ đề
            if topic_column != "Không chọn":
                st.subheader(f"Phân tích theo chủ đề: {topic_column}")
                topics = df[topic_column].unique()
                for topic in topics:
                    st.write(f"Chủ đề: {topic}")
                    topic_df = df[df[topic_column] == topic]
                    topic_sentiment_counts = topic_df['sentiment'].value_counts().reset_index()
                    topic_sentiment_counts.columns = ['Sentiment', 'Count']
                    fig = px.pie(topic_sentiment_counts, values='Count', names='Sentiment', 
                                title=f'Phân phối trạng thái cho {topic}',
                                color='Sentiment',
                                color_discrete_map={'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#bdc3c7', 'Irrelevant': 'black',
                                                    'Tích cực': '#2ecc71', 'Tiêu cực': '#e74c3c'})
                    st.plotly_chart(fig)
                    
                # Tạo biểu đồ cột so sánh các chủ đề
                st.subheader("So sánh trạng thái giữa các chủ đề")
                topic_comparison = df.groupby([topic_column, 'sentiment']).size().unstack(fill_value=0)
                topic_comparison_percentage = topic_comparison.div(topic_comparison.sum(axis=1), axis=0) * 100
                fig = px.bar(topic_comparison_percentage.reset_index(), x=topic_column, y=topic_comparison_percentage.columns,
                             title="So sánh phân phối trạng thái giữa các chủ đề",
                             labels={'value': 'Phần trăm', 'variable': 'Trạng thái'},
                             color_discrete_map={'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#bdc3c7', 'Irrelevant': 'black',
                                                 'Tích cực': '#2ecc71', 'Tiêu cực': '#e74c3c'})
                st.plotly_chart(fig)
    else:
        st.info("Vui lòng upload file CSV và chọn cột cần phân tích.")

# Thêm thông tin về ứng dụng
st.sidebar.header("Mô tả")
st.sidebar.info("Mô hình này sử dụng mô hình BERT để phân tích trạng thái của văn bản được đưa vào,"
                "Nó có thể xử lý văn bản đơn lẻ, nhiều văn bản được nhập thủ công hay nhiều văn bản từ 1 file CSV ")

# Thêm lịch sử phân tích cảm xúc
st.sidebar.header("Lịch sử phân tích")
history_df = load_history()
if not history_df.empty:
    st.sidebar.write(history_df)
else:
    st.sidebar.info("Không có văn bản nào được phân tích.")