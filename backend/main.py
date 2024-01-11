from typing import Union
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from algorithms.levenshtein import L_FormulaComparer
from algorithms.tokenizer import LatexTokenizer

app = FastAPI()
report = ""

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


@app.post("/api/check-similarity-base")
async def check_similarity_base(request: Request):
    return {"message": "Report generated successfully"}


@app.post("/api/check-similarity-two-files")
async def check_similarity(request: Request):
    global report
    body = await request.json()
    text1 = body["text1"]
    text2 = body["text2"]
    threshold = body["threshold"]
    algorithms = body["algorithms"]

    # Start of HTML report with CSS styles
    report = """
    <html>
    <head>
        <style>
            body {font-family: Arial, sans-serif;}
            h1 {color: #333;}
            p {font-size: 1.1em;}
        </style>
    </head>
    <body>
        <h1>Raport podobieństwa między wzorami z podanych plików</h1>
    """

    result = ""
    if "algorithm1" in algorithms:
        l_formula_comparer = L_FormulaComparer()
        result = l_formula_comparer.generate_report(text1, text2, threshold)
        report += f"<h2> Wyniki dla algorytmu levenshtein'a: </h2> <p> {result}</p>"
    if "algorithm2" in algorithms:
        # TODO: add Jaccard similarity to the html report
        pass
    if "algorithm3" in algorithms:
        # TODO: add Cosine similarity to the html report
        pass
    report += "</body></html>"

    return {"message": "Report generated successfully"}


@app.get("/api/report", response_class=HTMLResponse)
def get_report():
    global report
    print("Accessing /report endpoint")
    print("Report content:", report)
    return HTMLResponse(content=report)
