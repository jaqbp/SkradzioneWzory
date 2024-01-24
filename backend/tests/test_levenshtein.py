import os

from backend.algorithms.levenshtein import L_FormulaComparer
from backend.algorithms.tokenizer import LatexTokenizer

directory = os.path.abspath(os.path.dirname(__file__))
documents_directory = os.path.join(directory, "..", "documents")

DOCUMENTS = []

for _, _, files in os.walk(documents_directory):
    for file in files:
        with open(os.path.join(documents_directory, file), "r") as f:
            DOCUMENTS.append(f.read().strip())


def test_same_formulas() -> None:
    formula1 = "a * b"
    formula2 = "a*b"
    levenshtein = L_FormulaComparer()
    score = levenshtein.compare_formulas(formula1, formula2)
    assert score == 100.0


def test_not_related_formulas() -> None:
    formula1 = "a * h / 2"
    formula2 = "sin^2(x) + cos^2(x)"
    levenshtein = L_FormulaComparer()
    score = levenshtein.compare_formulas(formula1, formula2)
    assert score < 10
