from fastapi import FastAPI
from time import ctime
from random import random

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello my best students"}


@app.get("/home")
def home():
    return {"message": "Welcome to Home Page"}


@app.get("/random")
def generate_random_number():
    return {"message": random(),
            "current_time": ctime(),}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name.capitalize()}",
            "current_time": ctime(),}
