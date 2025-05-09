# 📝 Text & PDF Summarizer UI

A simple web application that allows users to paste text or upload a PDF document, then summarizes the content using a HuggingFace transformer model integrated with LangChain and displayed via a Gradio interface.

---

## 🚀 Key Features

- Input text manually or via PDF upload
- Extracts and summarizes PDF text using NLP
- User-friendly Gradio interface
- Uses pre-trained `facebook/bart-large-cnn` summarization model

---

## 🏗️ Project Architecture

- **Gradio**: Frontend interface to interact with the app
- **PyPDF2**: Extracts text from PDF files
- **LangChain**: Framework for managing LLM-based workflows
- **HuggingFace**: Provides transformer models like BART for summarization

---

## 🔧 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/text-pdf-summarizer-ui.git
   cd text-pdf-summarizer-ui
