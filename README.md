# 📝 Text & PDF Summarizer UI

A lightweight web application that allows users to paste text or upload a PDF document, then summarizes the content using a HuggingFace transformer model integrated with LangChain and displayed via a Gradio interface.

## 🚀 Key Features

- Input text manually or via PDF upload
- Extracts and summarizes PDF text using NLP
- User-friendly Gradio interface
- Uses pre-trained `facebook/bart-large-cnn` summarization model

## 🏗️ Project Architecture

- **Gradio**: Frontend interface to interact with the app
- **PyPDF2**: Extracts text from PDF files
- **LangChain**: Framework for managing LLM-based workflows
- **HuggingFace**: Provides transformer models like BART for summarization

## 🔧 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/text-pdf-summarizer-ui.git
   cd text-pdf-summarizer-ui

📁 Folder Example

text-pdf-summarizer-ui/

├── app.py

├── requirements.txt

└── README.md

1- Create a virtual environment (optional)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate

2- Install dependencies
   pip install -r requirements.txt

3- Run the app
   python app.py

🧠 About the Tools
   LangChain
   LangChain provides a modular framework for building applications with language models. Here, it's used to   manage prompting and model output formatting.

   HuggingFace Transformers
   We use the facebook/bart-large-cnn model, a powerful encoder-decoder model ideal for summarization.

   Gradio
   Gradio lets us quickly build and share user-friendly web interfaces for Machine Learning apps.

🔍 Implementation Details
   1- Model Initialization: Using HuggingFacePipeline via LangChain
   2- PromptTemplate: Wraps text for inference
   3- PDF Handling: Reads uploaded file as bytes and extracts text using PyPDF2
   4- UI Logic: Built with Gradio Blocks to control layout, input, and output

✅ Example Usage
   - Upload a PDF or paste article text
   - Cick “Convert PDF to Text” (if PDF)- 
   - Click “Summarize Text”
   - View summary below the input

📝 License
    MIT

🤝 Contributions
    Pull requests and suggestions welcome!





