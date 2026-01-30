#!/usr/bin/env python3
"""Convert PDF to PNG image"""
import sys

try:
    # Try PyMuPDF first (faster)
    import fitz

    def convert_with_pymupdf(pdf_path, output_path, dpi=300):
        doc = fitz.open(pdf_path)
        page = doc[0]
        mat = fitz.Matrix(dpi/72, dpi/72)
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_path)
        doc.close()
        print(f"Converted {pdf_path} to {output_path} using PyMuPDF")

    convert_func = convert_with_pymupdf

except ImportError:
    try:
        # Try pdf2image
        from pdf2image import convert_from_path
        from PIL import Image

        def convert_with_pdf2image(pdf_path, output_path, dpi=300):
            images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=1)
            images[0].save(output_path, 'PNG')
            print(f"Converted {pdf_path} to {output_path} using pdf2image")

        convert_func = convert_with_pdf2image

    except ImportError:
        print("Error: Neither PyMuPDF (fitz) nor pdf2image is installed.")
        print("Please install one of them:")
        print("  pip install PyMuPDF")
        print("  or")
        print("  pip install pdf2image (requires poppler)")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_pdf.py <input.pdf> <output.png> [dpi]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300

    convert_func(pdf_path, output_path, dpi)
