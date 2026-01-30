#!/usr/bin/env python3
"""
Convert Framework PDF to PNG using alternative methods
"""

import sys
import subprocess
import os

def convert_with_imagemagick(pdf_path, output_path, dpi=200):
    """Try ImageMagick's convert command"""
    try:
        cmd = [
            'convert',
            '-density', str(dpi),
            '-quality', '90',
            f'{pdf_path}[0]',  # First page only
            output_path
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Converted using ImageMagick: {output_path}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ ImageMagick failed: {e}")
        return False

def convert_with_ghostscript(pdf_path, output_path, dpi=200):
    """Try Ghostscript"""
    try:
        cmd = [
            'gs',
            '-dSAFER',
            '-dBATCH',
            '-dNOPAUSE',
            '-sDEVICE=png16m',
            f'-r{dpi}',
            '-dFirstPage=1',
            '-dLastPage=1',
            f'-sOutputFile={output_path}',
            pdf_path
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Converted using Ghostscript: {output_path}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ Ghostscript failed: {e}")
        return False

def main():
    pdf_path = "resorces/Framework_final.pdf"
    output_path = "assets/images/framework.png"

    if not os.path.exists(pdf_path):
        print(f"❌ Error: {pdf_path} not found")
        sys.exit(1)

    # Create output directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("Attempting to convert PDF to PNG...\n")

    # Try multiple methods
    methods = [
        ("ImageMagick (convert)", convert_with_imagemagick),
        ("Ghostscript (gs)", convert_with_ghostscript),
    ]

    for method_name, method_func in methods:
        print(f"Trying {method_name}...")
        if method_func(pdf_path, output_path, dpi=200):
            print(f"\n🎉 Success! Framework image saved to: {output_path}")
            print("\nNow updating index.html to use the PNG image instead of PDF iframe...")
            return 0

    print("\n⚠️  All conversion methods failed.")
    print("\nManual conversion options:")
    print("1. Install ImageMagick: sudo apt-get install imagemagick")
    print("2. Install Ghostscript: sudo apt-get install ghostscript")
    print("3. Use online converter: https://www.ilovepdf.com/pdf_to_jpg")
    print("4. Use Adobe Acrobat or other PDF viewer to export as PNG")
    print("\nThe current index.html uses PDF iframe which should work in most browsers.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
