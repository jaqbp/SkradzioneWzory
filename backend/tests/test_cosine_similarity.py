import os

from backend.algorithms.cosine_similarity import CSTextProcessor, CosineSimilarity


directory = os.path.abspath(os.path.dirname(__file__))
documents_directory = os.path.join(directory, "..", "documents")

DOCUMENTS = []

for _, _, files in os.walk(documents_directory):
    for file in files:
        with open(os.path.join(documents_directory, file), "r") as f:
            DOCUMENTS.append(f.read().strip())


def test_same_files() -> None:
    file1 = DOCUMENTS[0]
    file2 = DOCUMENTS[0]
    text_processor = CSTextProcessor({})
    words1 = text_processor.get_word_counts(file1)
    words2 = text_processor.get_word_counts(file2)
    score = CosineSimilarity.calculate_cosine_similarity(words1, words2)
    assert score == 100.0

def test_not_related_files() -> None:
    file1 = DOCUMENTS[0]
    file2 = DOCUMENTS[9]
    text_processor = CSTextProcessor({})
    words1 = text_processor.get_word_counts(file1)
    words2 = text_processor.get_word_counts(file2)
    score = CosineSimilarity.calculate_cosine_similarity(words1, words2)
    assert score < 5.0
