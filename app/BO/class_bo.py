# app/BO/classes_bo.py
from app.DAO.classes_dao import ClassesDAO
from sqlalchemy.orm import Session
from typing import List

class ClassesBO:
    def __init__(self, db: Session):
        self.db = db
        self.classes_dao = ClassesDAO()

    def create_class(self, name: str):
        existing_class = self.classes_dao.get_class_by_name(self.db, name)
        if existing_class:
            raise ValueError("Class with this name already exists.")
        
        return self.classes_dao.create_class(self.db, name)

    def list_classes(self, skip: int = 0, limit: int = 100) -> List[dict]:
        return self.classes_dao.get_classes(self.db, skip, limit)

    def remove_class(self, class_id: int):
        class_obj = self.classes_dao.get_class_by_id(self.db, class_id)
        if not class_obj:
            raise ValueError(f"Class with ID {class_id} not found.")
        
        return self.classes_dao.delete_class(self.db, class_id)

    def modify_class(self, class_id: int, name: str):
        # Kiểm tra xem lớp đã tồn tại chưa
        class_obj = self.classes_dao.get_class_by_id(self.db, class_id)
        if not class_obj:
            raise ValueError(f"Class with ID {class_id} not found.")
        
        # Cập nhật lớp học
        return self.classes_dao.update_class(self.db, class_id, name)
