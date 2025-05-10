# 📝 Text & PDF Summarizer UI

A lightweight web application that allows users to paste text or upload a PDF document, then summarizes the content using a HuggingFace transformer model integrated with LangChain and displayed via a Gradio interface.

Please see https://huggingface.co/spaces/rahimizadeh/text-pdf-summarizer-ui to run this app online!

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

**1- Clone the repo**
   ```bash
   git clone https://github.com/rahimizadeh/text-pdf-summarizer-ui.git
   cd text-pdf-summarizer-ui
 ```

&nbsp;&nbsp;&nbsp;📁**Project Structure**  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── text-pdf-summarizer-ui/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── app.py   &nbsp;&nbsp;&nbsp;# Application  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── requirements.txt               
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── README.md

**2- Create a virtual environment (optional)**
   ``` python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
 ```

**3- Install dependencies**

```bash
pip install -r requirements.txt
 ```

**4- Run the app**
```bash
python app.py
```


## 🧠 About the Tools

   &nbsp;**LangChain**: provides a modular framework for building applications with language models. Here, it's used to manage prompting and model output formatting.

   &nbsp;**HuggingFace Transformers**: We use the facebook/bart-large-cnn model, a powerful encoder-decoder model ideal for summarization.

   &nbsp;**Gradio**: lets us quickly build and share user-friendly web interfaces for Machine Learning apps.


## 🔍 Implementation Details

   &nbsp;&nbsp;&nbsp;1- Model Initialization: Using HuggingFacePipeline via LangChain
   
  &nbsp;&nbsp;&nbsp;2- PromptTemplate: Wraps text for inference
   
  &nbsp;&nbsp;&nbsp;3- PDF Handling: Reads uploaded file as bytes and extracts text using PyPDF2
   
  &nbsp;&nbsp;&nbsp;4- UI Logic: Built with Gradio Blocks to control layout, input, and output


## ✅ Example Usage
   - Upload a PDF or paste article text
   - Cick “Convert PDF to Text” (if PDF)- 
   - Click “Summarize Text”
   - View summary below the input

## 📝 License
    MIT

##  🤝 Contributions
    Pull requests and suggestions welcome!
