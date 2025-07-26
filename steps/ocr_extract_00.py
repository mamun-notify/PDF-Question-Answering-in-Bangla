# steps/ocr_extract_00.py
import os
from PIL import Image
import pytesseract

def extract_text_from_images(input_dir, output_file, lang='ben'):
    pytesseract.pytesseract.tesseract_cmd = r"D:\Tessarect\tesseract.exe"  # no quotes!

    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"❌ Input folder '{input_dir}' does not exist.")
    
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    all_text = []

    print("📝 Starting OCR extraction from images...")

    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            text = pytesseract.image_to_string(Image.open(image_path), lang=lang)
            all_text.append(text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(all_text))

    print(f"✅ OCR complete. Output saved to: {output_file}")
