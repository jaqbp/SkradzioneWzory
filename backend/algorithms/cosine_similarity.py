# TODO: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
import re
from collections import Counter
from typing import Set
from math import sqrt


class CSTextProcessor:
    def __init__(self, noise_words: Set[str]):
        self.noise = noise_words

    def prepare_text(self, text: str) -> str:
        punctuation_regex = re.compile(r"[\.,:;!\?]")
        noise_regex = re.compile(rf"\b({'|'.join(self.noise)})\b", re.IGNORECASE)
        multispace_regex = re.compile(r"\s+")

        cleaned_text = punctuation_regex.sub("", text)
        cleaned_text = noise_regex.sub("", cleaned_text)
        cleaned_text = multispace_regex.sub(" ", cleaned_text).lower()

        return cleaned_text

    def get_word_counts(self, text: str) -> Counter:
        cleaned_text = self.prepare_text(text)
        words = Counter(cleaned_text.split())
        return words


class CosineSimilarity:
    @staticmethod
    def calculate_cosine_similarity(words1: Counter, words2: Counter) -> float:
        numerator = sum(
            count * words2[word] for word, count in words1.items() if word in words2
        )
        denominator = (
            sqrt(sum(count**2 for count in words1.values())) ** 0.5
            * sqrt(sum(count**2 for count in words2.values())) ** 0.5
        )
        return numerator / denominator
