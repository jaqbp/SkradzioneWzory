import re
import sys
from collections import Counter

noise = {
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


def prepare_text(text: str) -> str:
    punctuation_regex = re.compile(r"[\.,:;!\?]")
    noise_regex = re.compile(rf"\b({'|'.join(noise)})\b", re.IGNORECASE)
    multispace_regex = re.compile(r"\s+")

    return multispace_regex.sub(
        " ", noise_regex.sub("", punctuation_regex.sub("", text))
    ).lower()


def main(argv=sys.argv) -> int:
    if len(argv) != 3:
        print("Usage: python main.py <file1> <file2>")
        return 1

    with open(argv[1]) as f1, open(argv[2]) as f2:
        text1 = f1.read().strip("\n")
        text2 = f2.read().strip("\n")

    text1 = prepare_text(text1)
    text2 = prepare_text(text2)

    words1 = Counter(text1.split())
    words2 = Counter(text2.split())

    # https://en.wikipedia.org/wiki/Cosine_similarity
    numerator = sum(
        count * words2[word]
        for word, count in words1.items()
        if word in words2
    )
    denominator = (
        sum(count**2 for count in words1.values()) ** 0.5
        * sum(count**2 for count in words2.values()) ** 0.5
    )
    print(numerator / denominator)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# TODO: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
