
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Table Header missing bracket
    # [표 3-2 -> [표 3-2]
    content = content.replace("[표 3-2 ", "[표 3-2] ")
    content = content.replace("[표 3-2\n", "[표 3-2]\n")
    
    # 2. Fix "elements)7는"
    # Use regex to be more robust
    content = re.sub(r"요소\(elements\).?7는", "요소가", content)
    content = re.sub(r"elements\).?7는", "요소가", content)
    
    # 3. Fix 1081 -> int
    content = content.replace("1081", "int")
    
    # 4. Fix any other "2]" -> "의" leftovers?
    # e.g. "dtype=int2" -> "dtype=int" ?
    # Line 379 in previous views: "dtype=int= 지정하면" -> "int로". "int2" might be "int로"?
    # Let's look for "int2"
    content = content.replace("int2", "int로")
    content = content.replace("float2", "float로")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 6 fixes.")

if __name__ == "__main__":
    main()
