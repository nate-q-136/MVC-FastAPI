from sqlalchemy.orm import Session
from typing import List
from app.DAO.classes_dao import ClassesDAO
from app.BO.base import BaseBO

class ClassesBO(BaseBO):
    def __init__(self, db: Session):
        """
        Dependency injection: db session and classes_dao are injected from outside.
        """
        super().__init__(db)  # Initialize the base class with the db session
        self.classes_dao = ClassesDAO()  # Injected DAO instance

    def create(self, name: str):
        # Check if class already exists
        existing_class = self.classes_dao.get_class_by_name(self.db, name)
        if existing_class:
            raise ValueError("Class with this name already exists.")
        
        # Create a new class
        return self.classes_dao.create_class(self.db, name)

    def list(self, skip: int = 0, limit: int = 100) -> List[dict]:
        # Return list of classes from DAO
        return self.classes_dao.get_classes(self.db, skip, limit)

    def delete(self, class_id: int):
        # Check if class exists
        class_obj = self.classes_dao.get_class_by_id(self.db, class_id)
        if not class_obj:
            raise ValueError(f"Class with ID {class_id} not found.")
        
        # Delete the class
        return self.classes_dao.delete_class(self.db, class_id)

    def update(self, class_id: int, name: str):
        # Check if class exists
        class_obj = self.classes_dao.get_class_by_id(self.db, class_id)
        if not class_obj:
            raise ValueError(f"Class with ID {class_id} not found.")
        
        # Update class name
        return self.classes_dao.update_class(self.db, class_id, name)
