# app/BO/student_bo.py
from app.DAO.students_dao import StudentDAO
from sqlalchemy.orm import Session
from typing import List

class StudentBO:
    def __init__(self, db: Session):
        self.db = db
        self.student_dao = StudentDAO()

    def create_student(self, full_name: str, email: str, password: str, class_id: int):
        # Thực hiện các kiểm tra logic nghiệp vụ trước khi tạo sinh viên
        if not full_name or not email or not password:
            raise ValueError("Full name, email, and password must be provided.")
        
        # Kiểm tra xem sinh viên đã tồn tại chưa
        existing_student = self.student_dao.get_student_by_email(self.db, email)
        if existing_student:
            raise ValueError("Student with this email already exists.")
        
        return self.student_dao.create_student(self.db, full_name, email, password, class_id)

    def list_students(self, skip: int = 0, limit: int = 100) -> List[dict]:
        # Logic nghiệp vụ để lấy danh sách sinh viên
        return self.student_dao.get_students(self.db, skip, limit)

    def remove_student(self, student_id: int):
        # Logic kiểm tra trước khi xóa sinh viên
        student = self.student_dao.get_student_by_id(self.db, student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        return self.student_dao.delete_student(self.db, student_id)

    def modify_student(self, student_id: int, full_name: str = None, email: str = None, password: str = None, class_id: int = None):
        # Logic để sửa thông tin sinh viên
        student = self.student_dao.get_student_by_id(self.db, student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        
        return self.student_dao.update_student(self.db, student_id, full_name, email, password, class_id)
