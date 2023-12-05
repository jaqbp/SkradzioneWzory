from tokenizer import LatexTokenizer


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

    def generate_report(self, latex_content1, latex_content2):  # self
        math_expression1 = set(self.tokenizer.extract_math(latex_content1))
        math_expression2 = set(self.tokenizer.extract_math(latex_content2))

        similarity = []
        with open("report.txt", "w") as report_file:
            for i, expr1 in enumerate(math_expression1, start=1):
                for j, expr2 in enumerate(math_expression2, start=1):
                    tokens1 = set(expr1)
                    tokens2 = set(expr2)

                    similarity.append(
                        self.jaccard_tanimoto_similarity(tokens1, tokens2)
                    )
                    average_similarity = sum(similarity) / len(similarity)

                    similarity_between = self.jaccard_tanimoto_similarity(
                        tokens1, tokens2
                    )
                    if similarity_between > 0.01:
                        report_file.write(
                            f"Similarity between Formula {i} in File 1 and Formula {j} in File 2: {similarity_between}\n"
                        )
