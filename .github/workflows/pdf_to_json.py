
import pdfplumber
import json
import sys
import base64
from io import BytesIO

def extract_pdf_text(pdf_bytes):
    text_data = []
    with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text_data.append(page.extract_text())
    return "\n".join(text_data)

if __name__ == "__main__":
       base64_pdf = sys.stdin.read().strip()
    pdf_bytes = base64.b64decode(base64_pdf)
    text = extract_pdf_text(pdf_bytes)

    result = {
        "SATIS_KODU": text.split("\n")[0] if text else "",
        "FIRMA_ADI": text.split("\n")[1] if len(text.split("\n")) > 1 else "",
        "URUN_KODU": text.split("\n")[2] if len(text.split("\n")) > 2 else ""
    }

