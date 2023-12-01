from pylatexenc.latex2text import LatexNodes2Text
from os.path import join


def main() -> int:
    with open(join("tex_files", "example.tex")) as f:
        latex = f.read().strip("\n")
    print(LatexNodes2Text().latex_to_text(latex).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
