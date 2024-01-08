from algorithms.tokenizer import LatexTokenizer


class L_FormulaComparer:
    def levenshtein(self, a, b):
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

    def normalize_formula(self, formula):
        return formula.replace(" ", "")

    def compare_formulas(self, formula1, formula2):
        formula1_norm = self.normalize_formula(formula1)
        formula2_norm = self.normalize_formula(formula2)
        distance = self.levenshtein(formula1_norm, formula2_norm)
        max_length = max(len(formula1_norm), len(formula2_norm))
        if max_length == 0:
            return 100.0
        return (1 - distance / max_length) * 100

    def compare_formulas_list(self, formulas1, formulas2):
        result = []
        for formula1 in formulas1:
            for formula2 in formulas2:
                result.append(self.compare_formulas(formula1, formula2))
        return result

    def generate_report(self, latex_content1, latex_content2, threshold):
        latex_tokenizer = LatexTokenizer()
        math1 = latex_tokenizer.extract_math(latex_content1)
        math2 = latex_tokenizer.extract_math(latex_content2)
        result = ""
        for i, formula1 in enumerate(math1):
            for j, formula2 in enumerate(math2):
                similarity = self.compare_formulas(formula1, formula2)
                print(threshold)
                if similarity > float(threshold):
                    result += f"Wykryto podobieństwo na poziomie {'%.2f'%(similarity)}% między formułą {i+1} z pierwszego dokumentu, a formułą {j+1} z drugiego dokumentu\n\n"
        if result == "":
            result = (
                "Nie wykryto podobieństw dla wzorów z podanych dokumentów przy progu: "
                + str(threshold)
                + "%"
            )

        return result
