import os
from ply import lex
from jt_algorithm import JT_LatexSimilarityAnalyser
from cosine_similarity import CSTextProcessor, CosineSimilarity
from levenshtein import L_FormulaComparer
from tokenizer import LatexTokenizer

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

    text1 = "Przykładowy tekst numer jeden."
    text2 = "Tekst przykładowy numer dwa."

    words1 = text_processor.get_word_counts(text1)
    words2 = text_processor.get_word_counts(text2)

    similarity = CosineSimilarity.calculate_cosine_similarity(words1, words2)
    print(f"Podobieństwo kosinusowe: {similarity}")

    # Jaccard-Tanimoto

    jt_latex_similarity_analyser = JT_LatexSimilarityAnalyser()
    latex_tokenizer = LatexTokenizer()

    file_path1 = os.path.join(os.path.dirname(__file__), "tex_files/example2.tex")
    with open(file_path1, "r") as file:
        latex_content1 = "".join(file.readlines())
    tokens1 = latex_tokenizer.extract_math(latex_content1)

    file_path2 = os.path.join(os.path.dirname(__file__), "tex_files/document2.tex")
    with open(file_path2, "r") as file:
        latex_content2 = "".join(file.readlines())
    tokens2 = latex_tokenizer.extract_math(latex_content2)

    similarity_values = []
    for token_set1 in tokens1:
        for token_set2 in tokens2:
            similarity = jt_latex_similarity_analyser.calculate_similarity(
                token_set1, token_set2
            )
            similarity_values.append(similarity)

    average_similarity = sum(similarity_values) / len(similarity_values)
    # jt_latex_similarity_analyser.generate_report(tokens1, tokens2)

    # Levenshtein

    file_path1 = os.path.join(os.path.dirname(__file__), "tex_files/example2.tex")
    with open(file_path1, "r") as file:
        latex_content1 = file.read()
    math1 = latex_tokenizer.extract_math(latex_content1)

    file_path2 = os.path.join(os.path.dirname(__file__), "tex_files/document2.tex")
    with open(file_path2, "r") as file:
        latex_content2 = file.read()
    math2 = latex_tokenizer.extract_math(latex_content2)

    l_formula_comparer = L_FormulaComparer()

    print("Formulas from the first document:", math1)
    print("Formulas from the second document:", math2)

    for i, formula1 in enumerate(math1):
        for j, formula2 in enumerate(math2):
            similarity = l_formula_comparer.compare_formulas(formula1, formula2)
            print(
                f"Similarity percentage between formula {i+1} from document 1 and formula {j+1} from document 2: {similarity:.2f}%"
            )
