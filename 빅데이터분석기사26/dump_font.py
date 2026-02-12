
import fitz
import sys

def dump_font_info(pdf_path, page_num=0):
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    blocks = page.get_text("dict")["blocks"]
    
    print(f"--- Page {page_num+1} Font Info ---")
    for block in blocks:
        if block["type"] == 0:
            for line in block["lines"]:
                for span in line["spans"]:
                    print(f"Text: '{span['text'][:20]}...' | Font: {span['font']} | Size: {span['size']} | Flags: {span['flags']}")

if __name__ == "__main__":
    dump_font_info(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0)
