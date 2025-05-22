from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students_data = []

@app.on_event("startup")
def load_data():
    global students_data
    csv_path = os.path.join(os.path.dirname(__file__), "..", "students.csv")
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        students_data = [
            {"studentId": int(row["studentId"]), "class": row["class"]}
            for row in reader
        ]

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    if class_:
        filtered = [s for s in students_data if s["class"] in class_]
    else:
        filtered = students_data
    return {"students": filtered}
