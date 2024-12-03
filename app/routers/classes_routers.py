# app/api/v1/classes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.BO.class_bo import ClassesBO
from app.repositories import IBORepository

api_classes_routers = APIRouter()

@api_classes_routers.post("/classes/")
def add_class(name: str, db: Session = Depends(get_db)):
    try:
        classes_bo = IBORepository(ClassesBO(db=db))
        new_class = classes_bo.create(name)
        return new_class
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_classes_routers.put("/classes/{class_id}")
def modify_class(class_id: int, name: str, db: Session = Depends(get_db)):
    classes_bo = IBORepository(ClassesBO(db=db))
    try:
        updated_class = classes_bo.update(class_id, name)
        return updated_class
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@api_classes_routers.delete("/classes/{class_id}")
def remove_class(class_id: int, db: Session = Depends(get_db)):
    classes_bo = IBORepository(ClassesBO(db=db))
    try:
        result = classes_bo.delete(class_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@api_classes_routers.get("/classes/")
def list_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes_bo = IBORepository(ClassesBO(db=db))
    return classes_bo.list(skip=skip, limit=limit)
