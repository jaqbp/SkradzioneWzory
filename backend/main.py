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
    l_formula_comparer = L_FormulaComparer()

    result = ""
    result = l_formula_comparer.generate_report(text1, text2)

    return {"similarity": result}
