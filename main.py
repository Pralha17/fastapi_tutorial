from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, Pro!"}

@app.get("/greet")
def greet():
    return {"message":"Hello Broo Proo!!!!!!!"}

@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):
    if age is None:
        return {"message": f"Hello {name}"}
    return {"message": f"Hello {name} you are {age} years old!"}


class Student(BaseModel):
    name: str
    age: int
    roll: str

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }
