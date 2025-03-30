from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from models import TodoModel
from database import engine, Sessionlocal
from sqlalchemy.orm import session

app = FastAPI()

TodoModel.metadata.create_all(bind=engine)


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoResposne(TodoBase):
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/todo', response_model=list[TodoResposne])
async def get_todos(db: session = Depends(get_db)):
    todo = db.query(TodoModel).all()
    return todo


@app.get("/todos/{todo_id}",response_model=TodoResposne)
async def get_todo(todo_id: int,db : session  = Depends(get_db)):
    t = db.query(TodoModel).filter(TodoModel.id == todo_id)
    print(t)
    return t.first()



@app.post("/create-todo",response_model=TodoResposne)
async def create_todo(newtodo: TodoBase,db : session = Depends(get_db)):
    db_todo = TodoModel(title = newtodo.title,desciption= newtodo.description,completed = newtodo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.delete("/todos/{todo_id}", response_model=TodoResposne)
async def delete_todo(todo_id: int, db: session = Depends(get_db)):

    t = db.query(TodoModel).filter(TodoModel.id == todo_id).first()  # Fetch the instance
    db.delete(t)  # Delete the instance, not the query
    db.commit()
    return t
