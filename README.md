# SkradzioneWzory

Projekt ma na celu stworzenie narzędzia do detekcji plagiatów w tekstach matematycznych. Narzędzie to skanuje katalog z plikami źródłowymi w formacie LaTeX, wyłuskuje z dokumentów wzory matematyczne, a następnie wywołuje zewnętrzny program oceniający podobieństwo, używając trzech algorytmów porównujących:  algorytmu Levenshteina, indeksu Jaccarda-Tanimoto oraz podobieństwa kosinusowego. Porówananie można dokonać pomiędzy plikami .tex znadującymi się w bazie dokumentów lub dwoma plikami wysłanymi przez użytkownika. Wyniki detekcji plagiatów są raportowane w formie HTML z wizualizacją wzorów.

## Set up project for development

```bash
    pip install -e .
```
