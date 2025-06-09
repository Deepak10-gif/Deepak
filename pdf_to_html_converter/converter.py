import io
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams


def convert_pdf_to_html(pdf_path: str, html_path: str) -> None:
    """Convert a PDF file to an HTML document.

    Parameters
    ----------
    pdf_path : str
        Path to the input PDF file.
    html_path : str
        Path where the resulting HTML file will be written.
    """
    laparams = LAParams()
    with open(pdf_path, "rb") as in_file, open(html_path, "w", encoding="utf-8") as out_file:
        extract_text_to_fp(in_file, out_file, laparams=laparams, output_type="html", codec="utf-8")


def convert_pdf_to_html_string(pdf_path: str) -> str:
    """Convert PDF to an HTML string and return it."""
    laparams = LAParams()
    output = io.StringIO()
    with open(pdf_path, "rb") as in_file:
        extract_text_to_fp(in_file, output, laparams=laparams, output_type="html", codec="utf-8")
    return output.getvalue()
