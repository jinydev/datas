import fitz

def analyze_pdf_layout(pdf_path, page_num=0):
    doc = fitz.open(pdf_path)
    page = doc[page_num]
    
    # Get text blocks with detailed info
    # "dict" gives us spans, fonts, sizes, etc.
    blocks = page.get_text("dict")["blocks"]
    
    print(f"--- Analysis of Page {page_num+1} ---")
    for b in blocks:
        if b['type'] == 0: # Text block
            print(f"Block: bbox={b['bbox']}")
            for line in b["lines"]:
                for span in line["spans"]:
                    print(f"  Text: '{span['text']}' | Font: {span['font']} | Size: {span['size']:.2f} | Color: {span['color']}")
    
if __name__ == "__main__":
    pdf_path = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/빅데이터분석기사26_실기1.pdf"
    analyze_pdf_layout(pdf_path, 2) # Check page 3 (index 2) as it had code/content mixed
