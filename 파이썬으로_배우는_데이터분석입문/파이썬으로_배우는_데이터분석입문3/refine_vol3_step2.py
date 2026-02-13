
import re
import sys

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md" # Overwrite directly

# 1. OCR Replacement Map
# Replacements for common OCR garbage in this specific document
replacements = {
    r"2081778": "ndarray",
    r"208178": "ndarray",
    r"2087787": "ndarray",
    r"4081785": "다차원 배열",
    r"0030@>": "ndarray",
    r"016/": "view",
    r"016\\": "view",
    r"016": "view", # Be careful, might match numbers. Use regex word boundary if needed, but '016' is rare enough as a standalone number here.
    r" SYHhomogeneous\)": " (homogeneous)",
    r" AB 한다": " 설명한다",
    r" WA array\?": " 내장함수 array()",
    r"388ㅁ860": "arange",
    r"46706": "dtype",
    r" g4\(elements\)": " 요소(elements)",
    r"<1032": "<U32",
    r"04006>": "Python>",
    r"SUBS": "표준",
    r"Unicode BAS": "Unicode 문자", # Guessing 'Sequences' or 'Bytes' or 'Chars'
    r"16-60010/": "Little-endian",
    r"78ㅁ86": "arange",
    r"01706": "설정",
    r"2040007\.3182086\(\)": "numpy.arange()",
    r"ㅁ01007\.1108208060\)": "numpy.linspace()",
    r"31878 with 7681418117-8208060\)": "분할 수(num)",
    r"868": "start",
    r"810272\]": "stop]",
    r"10820806\(\)": "linspace()",
    r"8162": "step",
    r"26708\(\)": "zeros()",
    r"06ㅁ608\(0\)": "ones()",
    r"0165\(\)": "ones()",
    r"6/6\(\)": "eye()",
    r"6760": "eye",
    r"01\[7206ㅋ170\\": "order", # Context: "키워드 인자 ...로". Maybe 'dtype'? No, order fits 'C', 'F'. Or 'optional'. 'dtype' fits 'int'. 
    r"4110\)": "full()",
    r"A#ASHE": "생성하는",
    r"26008 1166\(3\)": "zeros_like(a)",
    r"0766_16\(\)": "ones_like()",
    r"0ㅁ68\(\)": "ones()",
    r"600": "copy", # 복사(600) -> 복사(copy)
    r"6025": "copy", # 복사(6025) -> 복사(copy)
    r"608181": "scalar",
    r"670800881118": "broadcasting",
    r"0080086009": "broadcasting",
    r"1068 Algebra": "Linear Algebra",
    r"80000": "Random",
    r"1※60-8126": "fixed-size",
    r"13ㅁ82ㅁ20860": "transpose", # "축 ...로 13ㅁ...하면" -> transpose하면
    r"0ㅠ6180848": "metadata",
    r"010760910181": "multidimensional",
    r"BY\]": "서로", # Context "BY] 다른 배열" -> "서로 다른 배열"
    r"MAb": "연산", # "산술 곱하기 MAb" -> "연산"? "식"?
    r"Ath": "연산", 
    r"HEL": "코드는", # "다음 HEL" -> "다음 코드는"
    r"HES": "코드는",
    r"Has": "배열", # "다음 Has" -> "다음 배열"? or '함수'?
    r"HSS": "배열을", # "HSS 반환" -> "배열을 반환"
    r"Q=": "는", # "linspaceQ=" -> "linspace는"
    r"E ": "는 ", # "numpyE" -> "numpy는"
}

def clean_text(text):
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
        
    # Generic cleanup
    text = text.replace("numpy2", "numpy의")
    text = text.replace("numpy9", "numpy의")
    text = text.replace("numpy7}", "numpy가")
    text = text.replace("array7}", "array가")
    text = text.replace("x7}", "x가")
    text = text.replace("a7}", "a가")
    text = text.replace("v7}", "v가")
    text = text.replace("bE", "b는")
    text = text.replace("xE", "x는") 
    text = text.replace("yE", "y는")
    text = text.replace("a=", "a는") # Context dependent, but often "변수 a=" -> "변수 a는"
    text = text.replace("b=", "b는")
    text = text.replace("x=", "x는")
    text = text.replace("y=", "y는")
    
    # Fix specific garbled headers
    text = re.sub(r'^\s*68\s*', '### ', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*@\s*', '### ', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*®\s*', '### ', text, flags=re.MULTILINE)
    
    return text

def format_tables(lines):
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect table marker
        if line.strip().startswith("**[표"):
            new_lines.append(line)
            i += 1
            # Skip empty lines to find header
            while i < len(lines) and not lines[i].strip():
                new_lines.append(lines[i])
                i += 1
            
            # Now we expect header
            if i < len(lines):
                header = lines[i].strip()
                # Check if next line is separator
                if i + 1 < len(lines) and set(lines[i+1].strip()) == {'-'}:
                    # It's a table!
                    
                    # Heuristic to split columns. 
                    # Usually "Name  Desc". Split by 2+ spaces.
                    cols = re.split(r'\s{2,}', header)
                    
                    # Convert to markdown header
                    md_header = "| " + " | ".join(cols) + " |"
                    md_sep = "| " + " | ".join(["---"] * len(cols)) + " |"
                    
                    new_lines.append(md_header)
                    new_lines.append(md_sep)
                    
                    i += 2 # Skip header and sep line
                    
                    # Process rows
                    while i < len(lines):
                        row_line = lines[i].strip()
                        # Stop if empty line or new section header or image
                        if not row_line or row_line.startswith("#") or row_line.startswith("!["):
                            new_lines.append("")
                            break
                        
                        # Split row. Be careful not to split inside parenthesis if possible, 
                        # but simple split by 2+ spaces is a good start for this simple table.
                        row_cols = re.split(r'\s{2,}', row_line)
                        
                        # Align with header col count if possible
                        if len(row_cols) < len(cols):
                            # Maybe just one big desc?
                            # Or strict split failed.
                            # Fallback: simpler split
                            pass
                        
                        md_row = "| " + " | ".join(row_cols) + " |"
                        new_lines.append(md_row)
                        i += 1
                    continue
        
        new_lines.append(line)
        i += 1
    return new_lines

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean Text
    content = clean_text(content)
    
    # 2. Format Tables (Row by row processing)
    lines = content.split('\n')
    lines = format_tables(lines)
    
    # Write back
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Refined {output_file}")

if __name__ == "__main__":
    main()
