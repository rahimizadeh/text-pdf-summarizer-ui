"""Gradio text/PDF summarizer with cached Hugging Face model loading."""

from functools import lru_cache
from io import BytesIO

import gradio as gr
from PyPDF2 import PdfReader
from transformers import AutoTokenizer, pipeline

MODEL_ID = "facebook/bart-large-cnn"
MAX_INPUT_TOKENS = 900


@lru_cache(maxsize=1)
def get_tokenizer():
    return AutoTokenizer.from_pretrained(MODEL_ID)


@lru_cache(maxsize=1)
def get_summarizer():
    return pipeline("summarization", model=MODEL_ID, tokenizer=MODEL_ID)


def chunk_text(text: str, max_tokens: int = MAX_INPUT_TOKENS):
    tokenizer = get_tokenizer()
    token_ids = tokenizer.encode(text, add_special_tokens=False)
    return [
        tokenizer.decode(token_ids[i : i + max_tokens], skip_special_tokens=True)
        for i in range(0, len(token_ids), max_tokens)
    ]


def summarize_text(text: str, max_output_tokens: int = 150) -> str:
    text = (text or "").strip()
    if not text:
        return "Please enter or extract some text first."

    max_output_tokens = max(40, min(int(max_output_tokens), 300))
    min_output_tokens = max(10, min(max_output_tokens - 1, max_output_tokens // 4))
    summarizer = get_summarizer()

    chunks = chunk_text(text)
    partials = []
    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=max_output_tokens,
            min_length=min_output_tokens,
            do_sample=False,
            truncation=True,
        )[0]["summary_text"]
        partials.append(result)

    if len(partials) == 1:
        return partials[0]

    combined = " ".join(partials)
    if len(get_tokenizer().encode(combined, add_special_tokens=False)) <= MAX_INPUT_TOKENS:
        return summarizer(
            combined,
            max_length=max_output_tokens,
            min_length=min_output_tokens,
            do_sample=False,
            truncation=True,
        )[0]["summary_text"]

    return combined


def pdf_to_text(pdf_file):
    if pdf_file is None:
        return "Please upload a PDF file first."
    try:
        reader = PdfReader(BytesIO(pdf_file))
        text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
        return text or "No extractable text found in the PDF."
    except Exception as exc:
        return f"Error reading PDF: {exc}"


with gr.Blocks() as demo:
    gr.Markdown("## 📝 Text & PDF Summarizer")
    with gr.Row():
        text_input = gr.Textbox(
            label="Enter article text",
            lines=15,
            placeholder="Paste your article here...",
        )
        pdf_file = gr.File(label="Or upload PDF", file_types=[".pdf"], type="binary")

    max_tokens = gr.Number(label="Maximum summary tokens", value=150, precision=0)
    with gr.Row():
        convert_btn = gr.Button("Convert PDF to Text")
        summary_btn = gr.Button("Summarize Text")

    output_text = gr.Textbox(label="Summary", lines=10)
    convert_btn.click(fn=pdf_to_text, inputs=pdf_file, outputs=text_input)
    summary_btn.click(fn=summarize_text, inputs=[text_input, max_tokens], outputs=output_text)


if __name__ == "__main__":
    demo.launch()
