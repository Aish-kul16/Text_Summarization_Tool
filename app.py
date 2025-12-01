import streamlit as st
from transformers import pipeline

st.title("🧠 AI-Powered Text Summarization")
st.write("Summarize long paragraphs into short, meaningful text using a pre-trained NLP model.")

# Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()


text = st.text_area("📝 Paste your text here:", height=200, placeholder="Enter or paste text to summarize...")


max_len = st.slider("Select summary length (approx.):", 50, 300, 130)


if st.button("✨ Generate Summary"):
    if len(text.strip()) > 0:
        summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
        st.subheader("📘 Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text first!")

st.caption("Built with ❤️ using Python, Hugging Face Transformers, and Streamlit.")
