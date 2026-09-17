# Text & PDF Summarizer UI

A Gradio application for summarizing pasted text or text extracted from PDFs with `facebook/bart-large-cnn`.

## Improvements in this version

- The model and tokenizer are loaded once and cached.
- Long documents are split into tokenizer-aware chunks before summarization.
- PDF bytes are read in memory rather than written to undeleted temporary files.
- The UI describes generation length in tokens, not words.
- `requirements.txt` is correctly named and can be installed directly.

## Setup

```bash
git clone https://github.com/rahimizadeh/text-pdf-summarizer-ui.git
cd text-pdf-summarizer-ui
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Then open the local Gradio URL shown in the terminal.

## Usage

1. Paste text, or upload a PDF and click **Convert PDF to Text**.
2. Choose a maximum summary-token value (40-300 is supported by the UI logic).
3. Click **Summarize Text**.

For long documents the application summarizes chunks individually and then, when feasible, performs a final summary over the combined partial summaries.

## Quick checks

Syntax check:

```bash
python -m py_compile app.py
```

Import check:

```bash
python -c "import app; print('app import OK')"
```

The first real summarization downloads the Hugging Face model, so it requires internet access and may take longer than later requests.

## Online demo

A Hugging Face Space may be available at:
https://huggingface.co/spaces/rahimizadeh/text-pdf-summarizer-ui

## License

MIT
