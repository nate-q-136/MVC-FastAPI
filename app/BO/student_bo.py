# app/BO/student_bo.py
from app.DAO.students_dao import StudentDAO
from sqlalchemy.orm import Session
from typing import List
from app.BO.base import BaseBO

class StudentBO(BaseBO):
    def __init__(self, db: Session):
        super().__init__(db)
        self.student_dao = StudentDAO()

    def create(self, full_name: str, email: str, password: str, class_id: int):
        if not full_name or not email or not password:
            raise ValueError("Full name, email, and password must be provided.")
        
        existing_student = self.student_dao.get_student_by_email(self.db, email)
        if existing_student:
            raise ValueError("Student with this email already exists.")
        
        return self.student_dao.create_student(self.db, full_name, email, password, class_id)

    def list(self, skip: int = 0, limit: int = 100) -> List[dict]:
        return self.student_dao.get_students(self.db, skip, limit)

    def delete(self, student_id: int):
        student = self.student_dao.get_student_by_id(self.db, student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        return self.student_dao.delete_student(self.db, student_id)

    def update(self, student_id: int, full_name: str = None, email: str = None, password: str = None, class_id: int = None):
        student = self.student_dao.get_student_by_id(self.db, student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        
        return self.student_dao.update_student(self.db, student_id, full_name, email, password, class_id)
