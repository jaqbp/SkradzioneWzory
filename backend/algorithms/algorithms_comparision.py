import os
from levenshtein import L_FormulaComparer
from tokenizer import LatexTokenizer


# here we define the class for the algorithm comparision which
# will be used in the main.py file it uses all of the algorithms
# which we have implemented
class AlgorithmComparision:
    def __init__(self, noise_words):
        self.latex_tokenizer = LatexTokenizer()
        self.l_formula_comparer = L_FormulaComparer()
        # initialize objects of other algorithms which we have implemented

    def compare(self, latex_content1, latex_content2):
        # here we use the algorithms which we have implemented
        # and return the result
        pass
