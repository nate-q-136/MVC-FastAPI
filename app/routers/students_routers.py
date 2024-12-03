# app/api/v1/students.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.BO.student_bo import StudentBO

api_students_routers = APIRouter()

@api_students_routers.post("/students/")
def add_student(full_name: str, email: str, password: str, class_id: int, db: Session = Depends(get_db)):
    try:
        student_bo = StudentBO(db=db)
        student = student_bo.create_student(full_name, email, password, class_id)
        return student
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_students_routers.get("/students/")
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    student_bo = StudentBO(db=db)
    return student_bo.list_students(skip=skip, limit=limit)

@api_students_routers.delete("/students/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    student_bo = StudentBO(db=db)
    try:
        result = student_bo.remove_student(student_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@api_students_routers.put("/students/{student_id}")
def modify_student(student_id: int, full_name: str = None, email: str = None, password: str = None, class_id: int = None, db: Session = Depends(get_db)):
    student_bo = StudentBO(db=db)
    try:
        result = student_bo.modify_student(student_id, full_name, email, password, class_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
