from ply import lex
import os
import re


class L_FormulaComparer:
    @staticmethod
    def levenshtein(a, b):
        if not a:
            return len(b)
        if not b:
            return len(a)

        # Initialize a matrix of dimensions (len(a)+1) x (len(b)+1)
        matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

        # Initialize the first column and first row
        for i in range(len(a) + 1):
            matrix[i][0] = i
        for j in range(len(b) + 1):
            matrix[0][j] = j

        # Iterate through the matrix and update values
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if a[i - 1] == b[j - 1]:
                    cost = 0
                else:
                    cost = 1

                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1] + cost,
                )

        return matrix[-1][-1]

    @staticmethod
    def normalize_formula(formula):
        return formula.replace(" ", "")

    @staticmethod
    def compare_formulas(self, formula1, formula2):
        formula1_norm = self.normalize_formula(formula1)
        formula2_norm = self.normalize_formula(formula2)
        distance = self.levenshtein(formula1_norm, formula2_norm)
        max_length = max(len(formula1_norm), len(formula2_norm))
        if max_length == 0:
            return 100.0
        return (1 - distance / max_length) * 100
