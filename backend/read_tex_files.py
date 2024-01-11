from algorithms.tokenizer import LatexTokenizer
import os


class ReadTexFiles:
    def load_tex_files(directory):
        tex_contents = []

        # Check if the directory exists
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' not found.")
            return tex_contents

        # Loop through all files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".tex"):
                file_path = os.path.join(directory, filename)

                # Open and read the contents of the .tex file
                with open(file_path, "r", encoding="utf-8") as file:
                    tex_contents.append(file.read())

        return tex_contents
