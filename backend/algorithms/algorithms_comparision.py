import os
from jt_algorithm import JT_LatexSimilarityAnalyser
from cosine_similarity import CSTextProcessor, CosineSimilarity
from levenshtein import L_FormulaComparer
from tokenizer import LatexTokenizer


class AlgorithmComparision:
    def __init__(self, noise_words):
        self.noise_words = noise_words
        self.cs_text_processor = CSTextProcessor(self.noise_words)
        self.latex_tokenizer = LatexTokenizer()
        self.jt_latex_similarity_analyser = JT_LatexSimilarityAnalyser()
        self.l_formula_comparer = L_FormulaComparer()
