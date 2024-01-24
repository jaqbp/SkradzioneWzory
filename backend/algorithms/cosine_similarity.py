# TODO: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
import re
from collections import Counter
from typing import Set

from pylatexenc.latex2text import LatexNodes2Text

from backend.algorithms.tokenizer import LatexTokenizer


class CSTextProcessor:
    def __init__(self, noise_words: Set[str]):
        self.noise = noise_words

    def prepare_text(self, text: str) -> str:
        punctuation_regex = re.compile(r"[\.,:;!\?]")
        noise_regex = re.compile(rf"\b({'|'.join(self.noise)})\b", re.IGNORECASE)
        math_symbols_regex = re.compile(r"[\+-=\*]")

        cleaned_text = punctuation_regex.sub("", text)
        cleaned_text = noise_regex.sub("", cleaned_text)
        cleaned_text = math_symbols_regex.sub("", cleaned_text)
        return LatexNodes2Text().latex_to_text(cleaned_text.lower().strip())

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
            sum(count**2 for count in words1.values()) ** 0.5
            * sum(count**2 for count in words2.values()) ** 0.5
        )
        return numerator / denominator * 100 if denominator != 0 else 0

    def generate_report(self, latex_content1, latex_content2, file_number, threshold):
        latex_tokenizer = LatexTokenizer()
        math1 = latex_tokenizer.extract_math(latex_content1)
        math2 = latex_tokenizer.extract_math(latex_content2)
        text_processor = CSTextProcessor({})
        result = "Wykryto podobieństwa dla wzorów: <br>"
        for i, formula1 in enumerate(math1):
            for j, formula2 in enumerate(math2):
                if (len(formula1) > 5) and (len(formula2) > 5):
                    c1 = text_processor.get_word_counts(formula1)
                    c2 = text_processor.get_word_counts(formula2)
                    similarity = CosineSimilarity.calculate_cosine_similarity(c1, c2)
                    if similarity >= float(threshold) - 0.01:
                        result += f"Wykryto podobieństwo na poziomie {'%.2f'%(similarity)}% między formułą numer {i+1} z pliku pliku użytkownika postaci: \[  {math1[i]}  \]  a formułą z dokumentu z bazy postaci: \[ {math2[j]} \]  <br>"
        if result == "Wykryto podobieństwa dla wzorów: <br>":
            result = ""
        return result

    def generate_report_two_files(self, latex_content1, latex_content2, threshold):
        latex_tokenizer = LatexTokenizer()
        math1 = latex_tokenizer.extract_math(latex_content1)
        math2 = latex_tokenizer.extract_math(latex_content2)
        text_processor = CSTextProcessor({})
        result = "Wykryto podobieństwa dla wzorów z podanych dokumentów: <br>"
        for i, formula1 in enumerate(math1):
            for j, formula2 in enumerate(math2):
                if (len(formula1) > 5) and (len(formula2) > 5):
                    c1 = text_processor.get_word_counts(formula1)
                    c2 = text_processor.get_word_counts(formula2)
                    similarity = CosineSimilarity.calculate_cosine_similarity(c1, c2)
                    if similarity >= float(threshold) - 0.01:
                        result += f"Wykryto podobieństwo na poziomie {'%.2f'%(similarity)}% między formułą numer {i+1} postaci \[ {math1[i]} \]  z pierwszego dokumentu a formułą numer {j+1} postaci:  \[ {math2[j]} \]  z drugiego dokumentu <br>"
        if result == "Wykryto podobieństwa dla wzorów z podanych dokumentów: <br>":
            result = (
                "Nie wykryto podobieństw dla wzorów z podanych dokumentów przy progu: "
                + str(threshold)
                + "%"
            )
        return result
