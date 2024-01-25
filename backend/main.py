import os
from typing import Union

import uvicorn
from algorithms.cosine_similarity import CosineSimilarity
from algorithms.levenshtein import L_FormulaComparer
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from read_tex_files import ReadTexFiles

app = FastAPI(debug=True)
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

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


# checking similarity between every formula in the first file with formulas in files in the documents directory
@app.post("/api/check-similarity-base")
async def check_similarity_base(request: Request):
    global report
    body = await request.json()
    text1 = body["text1"]
    threshold = body["threshold"]
    algorithms = body["algorithms"]
    script_directory = os.path.dirname(os.path.abspath(__file__))
    documents_directory = os.path.join(script_directory, "documents")
    tex_contents = ReadTexFiles.load_tex_files(documents_directory)

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
        <h1>Raport podobieństwa między wzorami z podanego pliku a wzorami z dokumentów znajdujących się w bazie: </h1>
    """

    if "algorithm1" in algorithms:
        l_formula_comparer = L_FormulaComparer()
        for index, content in enumerate(tex_contents, start=1):
            result = l_formula_comparer.generate_report(
                text1, content, index, threshold
            )
            if result != "":
                report += f"<h2> Wyniki dla algorytmu levenshtein'a dla pliku {index}: </h2> <p> {result}</p>"

    if "algorithm2" in algorithms:
        jaccard_tanimoto = JT_LatexSimilarityAnalyser()
        for index, content in enumerate(tex_contents, start=1):
            result = jaccard_tanimoto.generate_report(
                text1, content, index, threshold
            )
            if result != "":
                report += f"<h2> Wyniki dla algorytmu jaccarda-tanimoto dla pliku {index}: </h2> <p> {result}</p>"
    if "algorithm3" in algorithms:
        cosine_similarity = CosineSimilarity()
        for index, content in enumerate(tex_contents, start=1):
            result = cosine_similarity.generate_report(text1, content, index, threshold)
            if result != "":
                report += f"<h2> Wyniki dla algorytmu podobieństwa cosinusowego dla pliku {index}: </h2> <p> {result}</p>"
    report += "</body></html>"
    report = report.replace("$", "")
    return {"message": "Report generated successfully"}


# checking similarity between every formula in the first file with formulas in the second file
@app.get("/api/report-base", response_class=HTMLResponse)
def get_report(request: Request):
    print("Accessing /report-base endpoint")
    return templates.TemplateResponse(
        "report_template.html", {"request": request, "report": report}
    )


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
        result = l_formula_comparer.generate_report_two_files(text1, text2, threshold)
        report += f"<h2> Wyniki dla algorytmu levenshtein'a: </h2> <p> {result}</p>"
    if "algorithm2" in algorithms:
        jaccard_tanimoto = JT_LatexSimilarityAnalyser()
        result = jaccard_tanimoto.generate_report(text1, text2)
        report += f"<h2> Wyniki dla algorytmu jaccarda-tanimoto: </h2> <p> {result}</p>"
    if "algorithm3" in algorithms:
        cosine_similarity = CosineSimilarity()
        result = cosine_similarity.generate_report_two_files(text1, text2, threshold)
        report += f"<h2> Wyniki dla algorytmu podobieństwa cosinusowego: </h2> <p> {result}</p>"
    report += "</body></html>"
    report = report.replace("$", "")
    return {"message": "Report generated successfully"}


@app.get("/api/report-two-files", response_class=HTMLResponse)
def get_report(request: Request):
    print("Accessing /report-two-files endpoint")
    return templates.TemplateResponse(
        "report_template.html", {"request": request, "report": report}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
