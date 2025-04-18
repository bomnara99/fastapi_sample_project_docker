from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schema import schemas
from app.model import models
from app.core import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    return db_user