# add_api.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add_numbers(a: int, b: int):
    result = a + b
    return {"a": a, "b": b, "result": result}
