
import re

input_file = "파이썬으로_배우는_데이터분석입문4.md"
output_file = "파이썬으로_배우는_데이터분석입문4.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "@" usages
    content = content.replace("axis=@", "axis=0")
    content = content.replace("range [@, 1)", "range [0, 1)")
    content = content.replace("array([[@,", "array([[0,")
    content = content.replace("array([@.,", "array([0.,")
    content = content.replace("array([@.", "array([0.")
    content = content.replace(" @.", " 0.")
    content = content.replace(" -@.", " -0.")
    content = content.replace("array([[1@,", "array([[10,") # Context check needed? Usually 10 if integer array
    content = content.replace("array([[2@,", "array([[20,")
    content = content.replace("array([[3@,", "array([[30,")
    content = content.replace("[3@,", "[30,")

    # 2. Fix function name corruptions
    content = content.replace("farray", "array")
    content = content.replace("arrav", "array")
    content = content.replace("ㅁ0.8680(", "np.stack(") 
    content = content.replace("0.087211[(", "np.dsplit(")
    content = content.replace("0.087211([", "np.dsplit(")
    content = content.replace("standard_noraml", "standard_normal") # Typo in OCR or source?

    # 3. Fix "3318", "3218" -> "axis" or "축"
    # Context: "3318에 지정한 축으로" -> "axis에 지정한 축으로" or "kwd axis"
    content = content.replace("3318", "axis")
    content = content.replace("3218", "axis")

    # 4. Fix specific garbage
    content = content.replace("ㅠㅠ ㅅㅅ ㅅㅅ ㄴㄴㅁㄴㅇㄴㅇㄴㅇㄴㆍ", "")
    content = content.replace("of ~ 나 @", "of")

    # 5. Fix "3-1" -> "3." in float arrays
    # Context: "array([2., 3-1)" -> "array([2., 3.])"
    content = content.replace("3-1)", "3.])") 
    content = content.replace("7-1)", "7.])")

    # 6. Fix "Generator(PCG64) at @x..." -> "Generator(PCG64) at 0x..."
    content = content.replace("at @x", "at 0x")
    
    # 7. Fix "WHS", "WS", "HHS" -> "배열" (if not fixed in step 1)
    content = content.replace("WHS", "배열")
    content = content.replace("WS", "배열")
    content = content.replace("HHS", "배열")

    # 8. Fix "np. stack" spaces
    content = content.replace("np. stack", "np.stack")
    content = content.replace("np. hsplit", "np.hsplit")
    content = content.replace("np,vsplit", "np.vsplit")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 2 fixes.")

if __name__ == "__main__":
    main()
