# from ply import lex
# import os

# # Define tokens for LaTeX commands
# tokens = ("COMMAND",   
#         "WORD", 
#         "OPEN_BRACE", 
#         "CLOSE_BRACE", 
#         "NEWLINE", 
#         "MATH_MODE_INLINE",
#         "MATH_MODE_DISPLAY",
#         "EQUATION_ENVIRONMENT")

# # Define regex for tokens
# t_MATH_MODE_INLINE = r"\$[^\$]*\$"
# t_MATH_MODE_DISPLAY = r"\\\[[^\]]*\\\]"
# t_EQUATION_ENVIRONMENT = r"\\begin\{equation\}.*?\\end\{equation\}"
# t_COMMAND = r"\\[a-zA-Z]+"
# t_WORD = r"[a-zA-Z]+"
# t_OPEN_BRACE = r"\{"
# t_CLOSE_BRACE = r"\}"

# def t_NEWLINE(t):
#     r"\n+"
#     t.lexer.lineno += len(t.value)
#     pass

# def t_error(t):
#     r"\S"
#     t.lexer.skip(1)

# # Define a lexer
# lexer = lex.lex()

# file_path1 = os.path.join(os.path.dirname(__file__), "tex_files/example2.tex")
# with open(file_path1, "r") as file:
#     latex_content1 = "".join(file.readlines())

# file_path2 = os.path.join(os.path.dirname(__file__), "tex_files/document2.tex")
# with open(file_path2, "r") as file:
#     latex_content2 = "".join(file.readlines())


# # Tokenize function to extract words while skipping LaTeX commands
# def extract_math(latex_content):
#     lexer.input(latex_content)
#     math_expressions = []
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         if tok.type in [
#             "MATH_MODE_INLINE",
#             "MATH_MODE_DISPLAY",
#             "EQUATION_ENVIRONMENT",
#         ]:
#             # Remove LaTeX markers from the beginning and end of the expression
#             cleaned_expression = tok.value
#             if cleaned_expression.startswith("\\["):
#                 cleaned_expression = cleaned_expression[2:]
#             if cleaned_expression.endswith("\\]"):
#                 cleaned_expression = cleaned_expression[:-2]
#             math_expressions.append(cleaned_expression.strip())
#     return math_expressions


# # Extract words
# math_expression1 = set(extract_math(latex_content1))
# math_expression2 = set(extract_math(latex_content2))

# # Jaccard-Tanimoto
# def jaccard_tanimoto_similarity(set1, set2):
#     intersection = len(set1.intersection(set2))
#     union = len(set1.union(set2))
#     return intersection / union if union != 0 else 0

# similarity = []
# # Execute code
# for i, expr1 in enumerate(math_expression1, start=1):
#     for j, expr2 in enumerate(math_expression2, start=1):
#         tokens1 = set(expr1)
#         tokens2 = set(expr2)
#         similarity.append(jaccard_tanimoto_similarity(tokens1, tokens2))
#         average_similarity = sum(similarity) / len(similarity)
# print(f"Similarity between first document and the second is {average_similarity}")

# with open("report.txt", "w") as report_file:
#     for i, expr1 in enumerate(math_expression1, start=1):
#         for j, expr2 in enumerate(math_expression2, start=1):
#             tokens1 = set(expr1)
#             tokens2 = set(expr2)
            
#             similarity.append(jaccard_tanimoto_similarity(tokens1, tokens2))
#             average_similarity = sum(similarity) / len(similarity)

#             similarity_between = jaccard_tanimoto_similarity(tokens1, tokens2)
#             if similarity_between > 0.49:
#                 report_file.write(f"Similarity between Formula {i} in File 1 and Formula {j} in File 2: {similarity_between}\n")

from ply import lex
import os

class JT_LatexTokenizer:
    def __init__(self):
        # Define tokens for LaTeX commands
        self.tokens = (
            "COMMAND",   
            "WORD", 
            "OPEN_BRACE", 
            "CLOSE_BRACE", 
            "NEWLINE", 
            "MATH_MODE_INLINE",
            "MATH_MODE_DISPLAY",
            "EQUATION_ENVIRONMENT"
        )

        # Define regex for tokens
        self.t_MATH_MODE_INLINE = r"\$[^\$]*\$"
        self.t_MATH_MODE_DISPLAY = r"\\\[[^\]]*\\\]"
        self.t_EQUATION_ENVIRONMENT = r"\\begin\{equation\}.*?\\end\{equation\}"
        self.t_COMMAND = r"\\[a-zA-Z]+"
        self.t_WORD = r"[a-zA-Z]+"
        self.t_OPEN_BRACE = r"\{"
        self.t_CLOSE_BRACE = r"\}"

        self.lexer = lex.lex()

    def extract_math(self, latex_content):
        self.lexer.input(latex_content)
        math_expressions = []
        while True:
            tok = self.lexer.token()
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

class JT_LatexSimilarityAnalyser:
    @staticmethod
    def jaccard_tanimoto_similarity(self, set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0

    @staticmethod
    def calculate_similarity(self, latex_content1, latex_content2): # self
        math_expression1 = set(self.extract_math(latex_content1))
        math_expression2 = set(self.extract_math(latex_content2))

        similarity = []
        for i, expr1 in enumerate(math_expression1, start=1):
            for j, expr2 in enumerate(math_expression2, start=1):
                tokens1 = set(expr1)
                tokens2 = set(expr2)
                similarity.append(self.jaccard_tanimoto_similarity(tokens1, tokens2))

        average_similarity = sum(similarity) / len(similarity) if similarity else 0
        return average_similarity

    @staticmethod
    def generate_report(self, latex_content1, latex_content2): # self
        math_expression1 = set(self.extract_math(latex_content1))
        math_expression2 = set(self.extract_math(latex_content2))

        similarity = []
        with open("report.txt", "w") as report_file:
            for i, expr1 in enumerate(math_expression1, start=1):
                for j, expr2 in enumerate(math_expression2, start=1):
                    tokens1 = set(expr1)
                    tokens2 = set(expr2)

                    similarity.append(self.jaccard_tanimoto_similarity(tokens1, tokens2))
                    average_similarity = sum(similarity) / len(similarity)

                    similarity_between = self.jaccard_tanimoto_similarity(tokens1, tokens2)
                    if similarity_between > 0.49:
                        report_file.write(f"Similarity between Formula {i} in File 1 and Formula {j} in File 2: {similarity_between}\n")