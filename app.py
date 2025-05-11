# Running on local URL:  http://127.0.0.1:7860

import gradio as gr                 # Gradio: for creating web-based user interfaces
import PyPDF2                      # PyPDF2: for reading PDF files
import tempfile                    # tempfile: to safely handle temporary files
from langchain.prompts import PromptTemplate        # LangChain: for managing prompt templates
from langchain_huggingface.llms import HuggingFacePipeline  # LangChain integration with HuggingFace models

# Define a summarization class
class TextSummarizer:
    def __init__(self):
        # Define the model to use for summarization
        self.model_id = "facebook/bart-large-cnn"

    def summarize_text(self, article_text, max_length=150, min_length=30):
        # Load a summarization pipeline with custom length settings
        llm = HuggingFacePipeline.from_model_id(
            model_id=self.model_id,
            task="summarization",
            # Generating consistent output
            pipeline_kwargs={
                "max_length": max_length,
                "min_length": min_length,
                "do_sample": False  # Deterministic output
            }
        )

       """ Generating diverse outputs
             pipeline_kwargs = {
                "max_length": 250,
                "do_sample": True,
                "temperature": 0.7,  # More creative
                "top_k": 50,         # Limit to top 50 tokens
                "top_p": 0.95        # Use nucleus sampling
            }"""

        # Create a basic prompt template that just passes the text
        prompt = PromptTemplate(input_variables=["document"], template="""{document}""")

        # Format the article text into the prompt
        prompt_input = prompt.format(document=article_text)

        # Generate the summary using the model
        summary = llm.__call__(prompt_input)

        # If the model returns a list of summaries, extract the actual summary text
        if isinstance(summary, list):
            return summary[0]['summary_text'] if 'summary_text' in summary[0] else str(summary[0])
        return str(summary)  # Fallback for other formats

# Function to extract text from an uploaded PDF
def pdf_to_text(pdf_file):
    try:
        # Create a temporary file to write the uploaded PDF bytes
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(pdf_file)      # Write raw bytes directly
            tmp.flush()              # Make sure data is written to disk

            # Use PyPDF2 to read and extract text
            reader = PyPDF2.PdfReader(tmp.name)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)

            # Return cleaned-up text or a message if extraction fails
            return text.strip() if text.strip() else "No extractable text found in the PDF."
    except Exception as e:
        return f"Error reading PDF: {str(e)}"  # Return readable error message

# Instantiate the summarizer class
summarizer = TextSummarizer()

# Summarize input with user-defined maximum length
def summarize_input(text, max_words):
    if not text.strip():
        return "Please enter or extract some text first."

    try:
        # Convert max_words input to integer
        max_length = int(max_words)
        # Set a safe minimum length for quality summaries
        min_length = max(30, max_length // 4)

        # Generate the summary
        return summarizer.summarize_text(text, max_length=max_length, min_length=min_length)
    except Exception as e:
        return f"Error during summarization: {str(e)}"

# Build the Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📝 Text & PDF Summarizer with Length Control")

    with gr.Row():
        # Text input for manually entering article
        text_input = gr.Textbox(label="Enter article text", lines=15, placeholder="Paste your article here...")

        # Upload input for PDF files
        pdf_file = gr.File(label="Or upload PDF", file_types=[".pdf"], type="binary")

    # User input for controlling max summary length
    max_words = gr.Number(label="Max summary word count", value=150, precision=0)

    with gr.Row():
        # Button to convert PDF to text
        convert_btn = gr.Button("Convert PDF to Text")
        # Button to generate the summary
        summary_btn = gr.Button("Summarize Text")

    # Textbox to display the summary output
    output_text = gr.Textbox(label="Summary", lines=10)

    # Link buttons to their respective functions
    convert_btn.click(fn=pdf_to_text, inputs=pdf_file, outputs=text_input)
    summary_btn.click(fn=summarize_input, inputs=[text_input, max_words], outputs=output_text)

# Launch the app if run directly
if __name__ == "__main__":
    demo.launch()
