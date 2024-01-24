import os
from backend.algorithms.jt_algorithm import JT_LatexSimilarityAnalyser
from backend.algorithms.cosine_similarity import CSTextProcessor, CosineSimilarity
from backend.algorithms.levenshtein import L_FormulaComparer
from backend.algorithms.tokenizer import LatexTokenizer

if __name__ == "__main__":
    # Cosine Similarity

    noise_words = {
        "o",
        "w",
        "a",
        "i",
        "lub",
        "na",
        "z",
        "do",
        "jest",
        "nie",
        "się",
        "jak",
        "tak",
        "że",
        "co",
        "te",
        "po",
        "za",
        "ale",
        "to",
        "od",
        "tym",
        "oraz",
        "ani",
        "lecz",
        "więc",
        "aby",
    }

    text_processor = CSTextProcessor(noise_words)

    file_path1 = os.path.join(os.path.dirname(__file__), "tex_files", "document1.tex")
    with open(file_path1, "r") as file:
        latex_content1 = "".join(file.readlines())

    file_path2 = os.path.join(os.path.dirname(__file__), "tex_files", "document3.tex")
    with open(file_path2, "r") as file:
        latex_content2 = "".join(file.readlines())

    words1 = text_processor.get_word_counts(latex_content1)
    words2 = text_processor.get_word_counts(latex_content2)

    similarity = CosineSimilarity.calculate_cosine_similarity(words1, words2)
    print(f"Podobieństwo kosinusowe: {similarity}")

    # Jaccard-Tanimoto
    print("Jaccard-Tanimoto")
    jt_latex_similarity_analyser = JT_LatexSimilarityAnalyser()
    latex_tokenizer = LatexTokenizer()

    tokens1 = latex_tokenizer.extract_math(latex_content1)
    tokens2 = latex_tokenizer.extract_math(latex_content2)

    similarity_values = []
    for token_set1 in tokens1:
        for token_set2 in tokens2:
            similarity = jt_latex_similarity_analyser.calculate_similarity(
                token_set1, token_set2
            )
            similarity_values.append(similarity)

    jt_latex_similarity_analyser.generate_report(latex_content1, latex_content2)

    average_similarity = jt_latex_similarity_analyser.calculate_similarity(
        latex_content1, latex_content2
    )
    print(f"Average Similarity: {average_similarity}")

    # Levenshtein
    print("Levenshtein")

    l_formula_comparer = L_FormulaComparer()
    print(l_formula_comparer.generate_report(latex_content1, latex_content2, 1, 0.3))
