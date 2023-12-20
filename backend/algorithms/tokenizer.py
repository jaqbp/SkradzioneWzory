from ply import lex


class LatexTokenizer:
    def __init__(self):
        # Token definitions for mathematical formulas and LaTeX commands
        self.tokens = (
            "MATH_MODE_INLINE",
            "MATH_MODE_DISPLAY",
            "EQUATION_ENVIRONMENT",
            "COMMAND",
            "OTHER",
        )

        self.t_MATH_MODE_INLINE = r"\$[^\$]*\$"
        self.t_MATH_MODE_DISPLAY = r"\\\[[^\]]*\\\]"
        self.t_EQUATION_ENVIRONMENT = r"\\begin\{equation\}.*?\\end\{equation\}"
        self.t_COMMAND = r"\\[a-zA-Z]+"
        self.t_ignore_OTHER = r"."

        self.lexer = lex.lex(module=self)

    def t_error(self, t):
        t.lexer.skip(1)

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
                cleaned_expression = tok.value
                if cleaned_expression.startswith("\\["):
                    cleaned_expression = cleaned_expression[2:]
                if cleaned_expression.endswith("\\]"):
                    cleaned_expression = cleaned_expression[:-2]
                math_expressions.append(cleaned_expression.strip())
        return math_expressions
