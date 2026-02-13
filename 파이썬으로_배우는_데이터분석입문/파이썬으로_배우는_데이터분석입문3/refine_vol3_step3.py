
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

replacements = {
    r"@\.": "0.",
    r"So\]": "축",
    r"SoA\]": "축의",
    r"YS": "요소를",
    r"SS": "열을",
    r"ASS": "실수를",
    r"Ase": "에서는",
    r"AW는": "값은",
    r"BS": "모두",
    r"GC는": "생성하는",
    r"G\+=": "함수",
    r"2\}": "는", # arange()2} -> arange()는
    r"2\]": "의", # numpy2] -> numpy의
    r"\}": "는", # numpy} -> numpy는
    r"S ": "를 ", # ndarrayS -> ndarray를
    r"S\n": "를\n",
    r"S\.": "를.",
    r"a=": "a는", # a= -> a는 (often used in text descriptions)
    r"x=": "x는",
    r"y=": "y는",
    r"b=": "b는",
    r"c=": "c는",
    r"\*\]4": "다.", # ".... *]4" -> ".... 다."
    r"7\|": "기", # (7| -> 기 (보기)
}

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for pattern, repl in replacements.items():
        # Use regex for safety on some short patterns
        if len(pattern) < 3 and '\\' not in pattern:
             # simple replace might be safer for char sequences if not regex
             pass 
        content = re.sub(pattern, repl, content)

    # Specific fix for "start=@" in code blocks or text
    content = content.replace("start=@", "start=0")
    content = content.replace("step?", "step은")
    content = content.replace("A는", "실수는") # "정수뿐 아니라 A는 가능" -> "실수는"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Polished {output_file}")

if __name__ == "__main__":
    main()
