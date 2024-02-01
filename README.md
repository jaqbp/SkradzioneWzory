# SkradzioneWzory

Projekt ma na celu stworzenie narzędzia do detekcji plagiatów w tekstach matematycznych. Narzędzie to skanuje katalog z plikami źródłowymi w formacie LaTeX, wyłuskuje z dokumentów wzory matematyczne, a następnie ocenia podobieństwo, używając trzech algorytmów porównujących: algorytmu Levenshteina, indeksu Jaccarda-Tanimoto oraz podobieństwa kosinusowego. Porówananie można dokonać pomiędzy plikami .tex znadującymi się w bazie dokumentów lub dwoma plikami wysłanymi przez użytkownika. Wyniki detekcji plagiatów są raportowane w formie HTML z wizualizacją wzorów.

English Description:

The project aims to create a tool for detecting plagiarism in mathematical texts. This tool scans a directory with LaTeX source files, extracts mathematical formulas from the documents, and then assesses similarity using three comparison algorithms: the Levenshtein algorithm, Jaccard-Tanimoto index, and cosine similarity. Comparison can be made between .tex files present in the document database or between two files submitted by the user. Plagiarism detection results are reported in HTML format with a visualization of formulas.

## Set up project for development

```bash
    pip install -e .
```
