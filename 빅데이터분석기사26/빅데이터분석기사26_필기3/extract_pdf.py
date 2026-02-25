from pypdf import PdfReader

reader = PdfReader("빅데이터분석기사26_필기3.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

with open("index_extracted.md", "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted {len(text)} characters to index_extracted.md")
