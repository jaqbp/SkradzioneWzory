import read_tex_files
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
documents_directory = os.path.join(script_directory, "documents")

if __name__ == "__main__":
    aux = read_tex_files.ReadTexFiles.load_tex_files(documents_directory)
    print(aux[1])
