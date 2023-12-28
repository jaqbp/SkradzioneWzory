    latex_content = "Twoja zawartość LaTeX"
    extracted_equations = extractor.extract_math(latex_content)

    for eq in extracted_equations:
        print(eq)
