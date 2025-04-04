import os
from pdf2image import convert_from_path
import easyocr
from PIL import Image

# === Step 1: Convert PDF to images ===
pdf_path = r"C:\Users\vasug\Desktop\humanai\ocr\ocr_project\ES-AHPHU - J-000312-0014 – 1579.pdf"

output_folder = "pages"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

images = convert_from_path(pdf_path, dpi=300)
print(f"Converted {len(images)} pages to images.")

for i, img in enumerate(images):
    img_path = os.path.join(output_folder, f"page_{i+1}.png")
    img.save(img_path)
    print(f"Saved {img_path}")

# === Step 2: Initialize EasyOCR Reader ===
reader = easyocr.Reader(['en'])
ocr_results = []

# === Step 3: OCR for each page ===
for i in range(len(images)):
    img_path = os.path.join(output_folder, f"page_{i+1}.png")
    print(f"Running OCR on {img_path}...")
    text_lines = reader.readtext(img_path, detail=0)
    page_text = "\n".join(text_lines)
    ocr_results.append(f"--- Page {i+1} ---\n{page_text}\n")

# === Step 4: Save text to file ===
with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.writelines(ocr_results)

print("✅ OCR complete. Output saved to 'ocr_output.txt'")
