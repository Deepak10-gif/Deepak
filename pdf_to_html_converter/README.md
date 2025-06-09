# PDF to HTML Converter

This project provides a simple command line utility for converting PDF files into HTML. It uses [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six) for parsing the PDF content.

## Installation

Before using the converter, install the required dependency:

```bash
pip install pdfminer.six
```

## Usage

Run the CLI script with the input PDF path and desired output HTML path:

```bash
python -m pdf_to_html_converter.cli example.pdf example.html
```

The resulting HTML will be saved to `example.html`.
