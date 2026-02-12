import fitz
import sys

def check_pdf(path):
    doc = fitz.open(path)
    page = doc[0]
    text = page.get_text()
    if len(text.strip()) > 50:
        print(f"{path}: Text layer detected.")
        print("Sample text:")
        print(text[:200])
    else:
        print(f"{path}: No significant text layer (likely scanned).")

if __name__ == "__main__":
    check_pdf(sys.argv[1])
