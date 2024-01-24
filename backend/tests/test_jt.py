import os

from backend.algorithms.jt_algorithm import JT_LatexSimilarityAnalyser


directory = os.path.abspath(os.path.dirname(__file__))
documents_directory = os.path.join(directory, "..", "documents")

DOCUMENTS = []

for _, _, files in os.walk(documents_directory):
    for file in files:
        with open(os.path.join(documents_directory, file), "r") as f:
            DOCUMENTS.append(f.read().strip())


# def test_same_files() -> None:
#     file1 = DOCUMENTS[0]
#     file2 = DOCUMENTS[0]
#     jt = JT_LatexSimilarityAnalyser()
#     score = jt.calculate_similarity(file1, file2)
#     assert score == 100.0
# 
# def test_not_related_files() -> None:
#     file1 = DOCUMENTS[0]
#     file2 = DOCUMENTS[9]
#     jt = JT_LatexSimilarityAnalyser()
#     score = jt.calculate_similarity(file1, file2)
#     assert score ==0

