from ply import lex
import os
import re


# File paths for LaTeX files
file_path1 = "tex_files/document1.tex"
file_path2 = "tex_files/document2.tex"

# Token definitions for mathematical formulas and LaTeX commands
tokens = (
    "MATH_MODE_INLINE",
    "MATH_MODE_DISPLAY",
    "EQUATION_ENVIRONMENT",
    "COMMAND",
    "OTHER",
)

# Regex definitions for tokens
t_MATH_MODE_INLINE = r"\$[^\$]*\$"
t_MATH_MODE_DISPLAY = r"\\\[[^\]]*\\\]"
t_EQUATION_ENVIRONMENT = r"\\begin\{equation\}.*?\\end\{equation\}"
t_COMMAND = r"\\[a-zA-Z]+"
t_ignore_OTHER = r"."  # Ignore other characters


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()


def extract_math(latex_content):
    lexer.input(latex_content)
    math_expressions = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type in [
            "MATH_MODE_INLINE",
            "MATH_MODE_DISPLAY",
            "EQUATION_ENVIRONMENT",
        ]:
            # Remove LaTeX markers from the beginning and end of the expression
            cleaned_expression = tok.value
            if cleaned_expression.startswith("\\["):
                cleaned_expression = cleaned_expression[2:]
            if cleaned_expression.endswith("\\]"):
                cleaned_expression = cleaned_expression[:-2]
            math_expressions.append(cleaned_expression.strip())
    return math_expressions


# Extracting mathematical formulas
with open(file_path1, "r") as file:
    latex_content1 = file.read()
math1 = extract_math(latex_content1)

with open(file_path2, "r") as file:
    latex_content2 = file.read()
math2 = extract_math(latex_content2)


def levenshtein(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)

    # Initialize a matrix of dimensions (len(a)+1) x (len(b)+1)
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Initialize the first column and first row
    for i in range(len(a) + 1):
        matrix[i][0] = i
    for j in range(len(b) + 1):
        matrix[0][j] = j

    # Iterate through the matrix and update values
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost,
            )

    return matrix[-1][-1]


def normalize_formula(formula):
    return formula.replace(" ", "")


def compare_formulas(formula1, formula2):
    formula1_norm = normalize_formula(formula1)
    formula2_norm = normalize_formula(formula2)
    distance = levenshtein(formula1_norm, formula2_norm)
    max_length = max(len(formula1_norm), len(formula2_norm))
    if max_length == 0:
        return 100.0
    return (1 - distance / max_length) * 100


print("Formulas from the first document:", math1)
print("Formulas from the second document:", math2)

for i, formula1 in enumerate(math1):
    for j, formula2 in enumerate(math2):
        similarity = compare_formulas(formula1, formula2)
        print(
            f"Similarity percentage between formula {i+1} from document 1 and formula {j+1} from document 2: {similarity:.2f}%"
        )
