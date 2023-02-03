from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello my best students"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
