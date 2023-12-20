from pylatexenc.latexwalker import (
    LatexWalker,
    LatexEnvironmentNode,
    LatexMathNode,
    LatexGroupNode,
)
import os


class LatexMathExtractor:
    def __init__(self):
        pass

    def extract_math(self, latex_content):
        walker = LatexWalker(latex_content)
        tokens, _, _ = walker.get_latex_nodes()

        equations = []
        for node in tokens:
            if isinstance(
                node, (LatexEnvironmentNode, LatexMathNode)
            ) and node.isNodeType("math"):
                equations.append(node.nodelist_to_latex())
            elif isinstance(node, LatexGroupNode) and node.isNodeType("math"):
                equations.append(node.nodelist_to_latex())

        return equations

    def load_and_extract_math(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            latex_content = file.read()

        return self.extract_math(latex_content)


file_name = "document1.tex"
folder_path = "tex_files"
full_path = os.path.join(folder_path, file_name)
extractor = LatexMathExtractor()
extracted_equations = extractor.load_and_extract_math(full_path)

print(extracted_equations)
for eq in extracted_equations:
    print(eq)
