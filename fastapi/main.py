from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Todo(BaseModel):
    id : int
    title : str
    description : Optional[str] = None
    completed : bool = False

todo = []
@app.get('/todo')
async def get_todos():
    return todo

@app.get("/todos/{todo_id}")
async def get_todo(todo_id : int):
    for t in todo:
        if t["id"] == todo_id:
            return t
    return {"msg" : "No todo found"}

@app.post("/create-todo")
async def create_todo(newtodo : Todo):
    todo.append(newtodo.model_dump())
    return todo[-1]

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id : int):
    for t in todo:
        if t["id"] == todo_id:
            todo.remove(t)
            return{"msg" , "todo deleted"}
    return {"error" : "todo not found"}