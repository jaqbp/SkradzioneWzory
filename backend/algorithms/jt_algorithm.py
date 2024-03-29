from backend.algorithms.tokenizer import LatexTokenizer


class JT_LatexSimilarityAnalyser:
    def __init__(self):
        self.tokenizer = LatexTokenizer()

    def jaccard_tanimoto_similarity(self, set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0

    def calculate_similarity(self, latex_content1, latex_content2):  # self
        math_expression1 = set(self.tokenizer.extract_math(latex_content1))
        math_expression2 = set(self.tokenizer.extract_math(latex_content2))

        similarity = []
        for i, expr1 in enumerate(math_expression1, start=1):
            for j, expr2 in enumerate(math_expression2, start=1):
                tokens1 = set(expr1)
                tokens2 = set(expr2)
                similarity.append(self.jaccard_tanimoto_similarity(tokens1, tokens2))

        average_similarity = sum(similarity) / len(similarity) if similarity else 0
        return average_similarity

    def generate_report(self, latex_content1, latex_content2, threshold):  # self
        result = "Wykryto podobieństwa dla wzorów: <br>"
        math1 = list(set(self.tokenizer.extract_math(latex_content1)))
        math2 = list(set(self.tokenizer.extract_math(latex_content2)))

        similarity = []
        for i, expr1 in enumerate(math1, start=1):
            for j, expr2 in enumerate(math2, start=1):
                tokens1 = set(expr1)
                tokens2 = set(expr2)

        for i, expr1 in enumerate(math1):
            for j, expr2 in enumerate(math2):
                tokens1 = set(expr1)
                tokens2 = set(expr2)
                similarity.append(
                    self.jaccard_tanimoto_similarity(tokens1, tokens2)
                )
                average_similarity = 100 * sum(similarity) / len(similarity) if similarity else 0
                if average_similarity >= float(threshold) - 0.01:
                    result += f"Wykryto podobieństwo na poziomie {'%.2f'%(average_similarity)}% między formułą numer {i+1} z pliku pliku użytkownika postaci: \[  {math1[i]}  \]  a formułą z dokumentu z bazy postaci: \[ {math2[j]} \]  <br>"
        if result == "Wykryto podobieństwa dla wzorów: <br>":
            result = ""
        return result
