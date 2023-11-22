from ply import lex
import os

# Jaccarda-Tanimoto
def jaccard_tanimoto_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Define tokens for LaTeX commands
tokens = (
    'COMMAND',
    'WORD',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'NEWLINE'
)

# Define regex for tokens
t_COMMAND = r'\\[a-zA-Z]+'
t_WORD = r'[a-zA-Z]+'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
    r'\S'
    t.lexer.skip(1)

# Define a lexer
lexer = lex.lex()

file_path1 = os.path.join(os.path.dirname(__file__), 'tex_files/example.tex')
with open(file_path1, 'r') as file:
    latex_content1 = ''.join(file.readlines())

file_path2 = os.path.join(os.path.dirname(__file__), 'tex_files/example3.tex')
with open(file_path2, 'r') as file:
    latex_content2 = ''.join(file.readlines())

# Tokenize function to extract words while skipping LaTeX commands
def extract_words(latex_content):
    lexer.input(latex_content)
    words = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'WORD':
            words.append(tok.value)
    return words

# Extract words
words1 = set(extract_words(latex_content1))
words2 = set(extract_words(latex_content2))
# print(words1)

# Execution of code
similarity = jaccard_tanimoto_similarity(words1, words2)
print("Jaccard-Tanimoto Similarity:", similarity)