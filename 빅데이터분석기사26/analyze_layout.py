
import fitz
import sys

def analyze_layout(pdf_path):
    doc = fitz.open(pdf_path)
    # Check first few pages
    for i in range(min(3, len(doc))):
        page = doc[i]
        blocks = page.get_text("blocks")
        print(f"--- Page {i+1} ---")
        for b in blocks: # Print all blocks
            # b is (x0, y0, x1, y1, text, block_no, block_type)
            if b[0] > 300: # Highlight right-side blocks
                 print(f"RIGHT SIDE - BBox: {b[:4]} - Text: " + b[4][:20].replace('\n', ' ') + "...")
            else:
                 print(f"LEFT SIDE - BBox: {b[:4]} - Text: " + b[4][:20].replace('\n', ' ') + "...")

if __name__ == "__main__":
    analyze_layout(sys.argv[1])
