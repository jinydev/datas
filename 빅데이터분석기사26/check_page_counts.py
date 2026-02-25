import os
from pypdf import PdfReader

base_path = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26"
files = [
    "빅데이터분석기사26_필기1/빅데이터분석기사26_필기1.pdf",
    "빅데이터분석기사26_필기2/빅데이터분석기사26_필기2.pdf",
    "빅데이터분석기사26_필기3/빅데이터분석기사26_필기3.pdf",
    "빅데이터분석기사26_필기4/빅데이터분석기사26_필기4.pdf"
]

for rel_path in files:
    full_path = os.path.join(base_path, rel_path)
    if os.path.exists(full_path):
        try:
            reader = PdfReader(full_path)
            print(f"{rel_path}: {len(reader.pages)} pages")
        except Exception as e:
            print(f"{rel_path}: Error {e}")
    else:
        print(f"{rel_path}: File not found")
