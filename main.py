from fastapi import FastAPI
from time import ctime

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello my best students"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name.capitalize()}",
            "current_time": ctime(),}
