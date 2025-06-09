import argparse
from .converter import convert_pdf_to_html


def main():
    parser = argparse.ArgumentParser(description="Convert PDF file to HTML")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("html_path", help="Destination HTML file path")
    args = parser.parse_args()
    convert_pdf_to_html(args.pdf_path, args.html_path)


if __name__ == "__main__":
    main()
