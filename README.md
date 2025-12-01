# 🧠 AI-Powered Text Summarization Tool

This tool summarizes long text into short, meaningful content using Python, Streamlit, 
and a pre-trained NLP model (facebook/bart-large-cnn). It is simple, fast, and easy to run locally.

## 🚀 Features
- Summarizes large paragraphs into concise text
- Clean and interactive Streamlit UI
- Adjustable summary length
- Uses a powerful transformer model
- Beginner-friendly and lightweight

## 🛠️ Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- Torch

## 📦 Installation

# Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# If requirements.txt doesn't exist:
pip install streamlit transformers torch

## ▶️ Run the Application

streamlit run app.py


## 📂 Project Structure

app.py
README.md
.gitignore
requirements.txt   (optional)
venv/              (ignored)


## 🔮 Future Enhancements
- Add multiple summarization modes
- Summarize PDFs / DOCX files
- Summarize URLs / web pages
- Add multilingual support
- Cloud deployment option
