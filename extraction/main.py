import re


def read_latex_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def separate_math_text(latex_content):
    # Regex patterns to find math
    inline_math_pattern = re.compile(r"(\$(.*?)\$|\\\((.*?)\\\))")
    display_math_pattern = re.compile(
        r"(\$\$(.*?)\$\$|\\\[([\s\S]*?)\\\]|\\begin\{equation\}([\s\S]*?)\\end\{equation\})"
    )

    # Find all math expressions
    inline_math = inline_math_pattern.findall(latex_content)
    display_math = display_math_pattern.findall(latex_content)

    # Extract only the math parts from the matches
    inline_math = [m[1] or m[3] for m in inline_math]
    display_math = [m[1] or m[2] or m[3] for m in display_math]

    # Remove the math expressions from the text
    text_without_math = inline_math_pattern.sub("", latex_content)
    text_without_math = display_math_pattern.sub("", text_without_math)

    return inline_math, display_math, text_without_math


def save_results(inline_math, display_math, text_without_math):
    with open("inline_math.txt", "w", encoding="utf-8") as file:
        for item in inline_math:
            file.write(item + "\n")

    with open("display_math.txt", "w", encoding="utf-8") as file:
        for item in display_math:
            file.write(item + "\n")

    with open("text_without_math.txt", "w", encoding="utf-8") as file:
        file.write(text_without_math)


if __name__ == "__main__":
    latex_content = read_latex_file("example.tex")
    inline_math, display_math, text_without_math = separate_math_text(latex_content)
    save_results(inline_math, display_math, text_without_math)
