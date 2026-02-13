
import re

input_file = "파이썬으로_배우는_데이터분석입문5.md"
output_file = "파이썬으로_배우는_데이터분석입문5.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "@" in floats and other contexts
    # "@." -> "0."
    content = content.replace("@.", "0.")
    content = content.replace(" @.", " 0.")
    content = content.replace("(@.", "(0.")
    content = content.replace("=@.", "=0.")
    content = content.replace("lw=@.", "lw=0.")
    content = content.replace("alpha=@.", "alpha=0.")
    
    # 2. Fix Matplotlib function calls
    content = content.replace("plt. show()", "plt.show()")
    content = content.replace("p1t.show()", "plt.show()") # "p1t" typo
    content = content.replace("plt.plot([", "plt.plot([") # formatting check
    
    # 3. Fix "marker='0'" -> "marker='o'"
    # Context: plt.plot(..., marker='0') -> usually circle marker 'o'
    content = content.replace("marker='0'", "marker='o'")
    content = content.replace("marker='@'", "marker='o'")

    # 4. Fix specific text corruptions
    content = content.replace("numpy] 있는", "numpy에 있는")
    content = content.replace("ndenumerate(arr)_", "ndenumerate(arr)는")
    content = content.replace("1ㅁ06, 로", "index, value로") # "1ㅁ06" -> index? value?
    content = content.replace("p1t.", "plt.")

    # 5. Fix "Section ..." footers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)

    # 6. Fix "np.random.seed(2@25)" -> "2025" or similar
    content = re.sub(r"seed\(2@(\d+)\)", r"seed(20\1)", content)

    # 7. Fix "plt.title" garbage
    # "plt.title('2/A1 그래프 그리기')" -> "plt.title('직선 그래프 그리기')" ? 
    # Context: "직선 그래프 그리기" header above.
    
    # 8. Fix "68" -> "###" headers if applicable
    content = re.sub(r"^68\s+", "### ", content, flags=re.MULTILINE)
    content = re.sub(r"^\s*\|\s*\*\s*", "- ", content, flags=re.MULTILINE) # Table garbage to list?

    # 9. Clean up "![Image]..." spacing
    content = re.sub(r"(!\[Image\]\(.*?\))\s+", r"\1\n\n", content)

    # 10. Fix "ax.text(@.1, ...)" -> "ax.text(0.1, ...)"
    # Covered by #1 generally, but specific check:
    content = content.replace("ax.text(@", "ax.text(0")

    # 11. Fix "wspace=@, hspace=@" -> "wspace=0, hspace=0"
    content = content.replace("wspace=@", "wspace=0")
    content = content.replace("hspace=@", "hspace=0")

    # 12. Fix "p = [0.15, @.25, @.3, 0.1, @.1, @.1])" -> "0.25", "0.3", "0.1", "0.1"
    # Covered by #1.

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
