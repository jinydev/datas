
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Section 1: Specific Context Fixes (from grep analysis) ---

    # Fix "344235 5336; ..." garbled block to [50, 51, ...] style if possible, or just standard array output
    # Context linspace/reshape example.
    # It seems to be x[0, :], x[1, :], ...
    # Let's replace the completely broken lines with a placeholder or reconstructed valid output if we can infer it.
    # Found: "344235 5336; 37.-38. 739 [42, 43, 44, 45, 46, 47], [5@, 51, 52, 53, 54, 55]])"
    # This looks like rows of an 8x8 array (0..63).
    # Row 5: 40-47, Row 6: 48-55?
    # Let's try to fix the array syntax to be valid python-like representation.
    content = content.replace("344235 5336; 37.-38. 739", "[32, 33, 34, 35, 36, 37, 38, 39],")
    content = content.replace("[5@,", "[50,")

    # Fix "x[array([@, 2, 4]), array([@, 1])]" -> "x[array([0, 2, 4]), array([0, 1])]"
    content = content.replace("array([@,", "array([0,")
    content = content.replace("array([®,", "array([0,")

    # Fix "aa Dio ch In fu off Bo ow re 쏘 (으 10 Hu me xX Ne는 ott (Se)..."
    # This is pure garbage. Deleting it.
    content = re.sub(r"aa Dio ch In fu off Bo ow re.*?\n", "", content)

    # Fix "a[2:4, 3:7] apray([[19; 26, 21, 227, [27, 28, 29, 30]])"
    # -> "array([[19, 20, 21, 22], [27, 28, 29, 30]])"
    # Wait, simple fix for "apray"
    content = content.replace("apray", "array")
    content = content.replace("[19; 26, 21, 227,", "[19, 20, 21, 22],")

    # Fix "3[0808086(2, 5)][:, [1, 0, 3, 5]]" -> "a[arange(2, 5)][:, [1, 0, 3, 5]]"
    content = re.sub(r"0808086", "arange", content)
    
    # Fix "x = array([@, 10, 20, 30])" -> "x = array([0, 10, 20, 30])"
    content = content.replace("array([@,", "array([0,")

    # Fix "Index는rror" -> "IndexError"
    content = content.replace("Index는rror", "IndexError")
    
    # Fix "Ge 복사" -> "참조(Reference) 복사" (from previous step if not applied, or variations)
    # Check "27] (view)7는" -> "(view)가"
    content = content.replace("(view)7는", "(view)가")
    
    # Fix "ndarray》" -> "ndarray"
    content = content.replace("ndarray》", "ndarray")
    content = content.replace("08.002》(", "슬라이싱") # redundancy check
    
    # Fix "arnay" -> "array"
    content = content.replace("arnay", "array")

    # Fix "108178》에서" -> "ndarray에서"
    content = content.replace("108178》에서", "ndarray에서")
    
    # Fix "116, 17, ... 3911)" -> "39]]"
    content = content.replace("3911)", "39]]")
    content = content.replace("3111)", "31]]") # "31]]"

    # Fix "re 쏘 (으 10 Hu..." line if regex missed
    # It seems scanned earlier.

    # Fix "20.ㅁ6\8338" -> "np.newaxis" regex catch
    content = re.sub(r"20\.ㅁ6\\8338", "np.newaxis", content)
    
    # Fix "3318 1" -> "axis 1" (or "1축")
    content = content.replace("3318 1", "축 1")
    
    # Fix "70ㅁ6" -> "동일하"
    content = content.replace("70ㅁ6", "동일하")

    # Fix "ㅁ[0-9]" patterns globally where possible
    # "ㅁ41ㅁ7》" -> "이것은"
    content = content.replace("ㅁ41ㅁ7》", "이것은")
    
    # Fix "Python>" -> "Python"
    content = content.replace("Python>", "Python")

    # Fix "dtype=floato®" -> "dtype=float로"
    content = content.replace("floato®", "float로")
    
    # Fix "int는이면" -> "int이면"
    content = content.replace("int는이면", "int이면")

    # Fix "내잠함수" -> "내장함수"
    content = content.replace("내잠함수", "내장함수")
    
    # Fix "arangel)" -> "arange()"
    content = content.replace("arangel)", "arange()")
    
    # Fix "arange(56).reshape(7, 8)" -> "arange(56).reshape(7, 8)" (Valid)
    # But output below "x arnay([[ @, 1. 2, 3, 4, 5, 6, 71," needs fix
    # "71," -> "7],"
    content = content.replace("71,", "7],")
    content = content.replace("[ @,", "[ 0,")

    # Fix "Section 07 + 고급색인 _ 141" -> Remove or format
    # Likely page header/footer artifcat. Remove it.
    content = re.sub(r"Section \d+ \+ .*?_\s*\d+", "", content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with comprehensive Step 9 fixes.")

if __name__ == "__main__":
    main()
