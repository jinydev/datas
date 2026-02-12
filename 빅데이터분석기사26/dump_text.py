import fitz
import sys

def dump_text(path, page_num=0):
    doc = fitz.open(path)
    page = doc[page_num]
    text = page.get_text("blocks")
    for block in text:
        print(block)

if __name__ == "__main__":
    dump_text(sys.argv[1], int(sys.argv[2]))
