# app/DAO/students_dao.py
from sqlalchemy.orm import Session
from app.models.students import Students
from typing import List, Optional

class StudentDAO:
    
    @staticmethod
    def create_student(db: Session, full_name: str, email: str, password: str, class_id: int):
        db_student = Students(full_name=full_name, email=email, password=password, class_id=class_id)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    @staticmethod
    def get_students(db: Session, skip: int = 0, limit: int = 100) -> List[Students]:
        return db.query(Students).offset(skip).limit(limit).all()

    @staticmethod
    def get_student_by_id(db: Session, student_id: int) -> Optional[Students]:
        return db.query(Students).filter(Students.id == student_id).first()

    @staticmethod
    def get_student_by_email(db: Session, email: str) -> Optional[Students]:
        return db.query(Students).filter(Students.email == email).first()

    @staticmethod
    def delete_student(db: Session, student_id: int):
        student = db.query(Students).filter(Students.id == student_id).first()
        if student:
            db.delete(student)
            db.commit()
            return {"message": f"Student {student_id} deleted."}
        return {"message": "Student not found."}

    @staticmethod
    def update_student(db: Session, student_id: int, full_name: str = None, email: str = None, password: str = None, class_id: int = None):
        student = db.query(Students).filter(Students.id == student_id).first()
        if student:
            if full_name:
                student.full_name = full_name
            if email:
                student.email = email
            if password:
                student.password = password
            if class_id:
                student.class_id = class_id
            db.commit()
            db.refresh(student)
            return student
        return {"message": "Student not found."}
