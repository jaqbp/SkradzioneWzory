from typing import Union

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from algorithms.levenshtein import L_FormulaComparer
from algorithms.tokenizer import LatexTokenizer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/api/check-similarity")
async def check_similarity(request: Request):
    body = await request.json()
    text1 = body["text1"]
    text2 = body["text2"]

    latex_tokenizer = LatexTokenizer()
    math1 = latex_tokenizer.extract_math(text1)
    math2 = latex_tokenizer.extract_math(text2)

    l_formula_comparer = L_FormulaComparer()

    result = ""
    for i, formula1 in enumerate(math1):
        for j, formula2 in enumerate(math2):
            similarity = l_formula_comparer.compare_formulas(formula1, formula2)
            if similarity > 30:
                result += f"Wykryto podobieństwo na poziomie {'%.2f'%(similarity)}% między formułą {i+1} z pierwszego dokumentu, a formułą {j+1} z drugiego dokumentu\n\n"

    return {"similarity": result}
