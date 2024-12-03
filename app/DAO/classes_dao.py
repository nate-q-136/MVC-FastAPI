# app/DAO/classes_dao.py
from sqlalchemy.orm import Session
from app.models.classes import Classes
from typing import List, Optional

class ClassesDAO:

    @staticmethod
    def create_class(db: Session, name: str):
        db_class = Classes(name=name)
        db.add(db_class)
        db.commit()
        db.refresh(db_class)
        return db_class

    @staticmethod
    def get_classes(db: Session, skip: int = 0, limit: int = 100) -> List[Classes]:
        return db.query(Classes).offset(skip).limit(limit).all()

    @staticmethod
    def get_class_by_id(db: Session, class_id: int) -> Optional[Classes]:
        return db.query(Classes).filter(Classes.id == class_id).first()

    @staticmethod
    def get_class_by_name(db: Session, name: str) -> Optional[Classes]:
        return db.query(Classes).filter(Classes.name == name).first()

    @staticmethod
    def delete_class(db: Session, class_id: int):
        class_obj = db.query(Classes).filter(Classes.id == class_id).first()
        if class_obj:
            db.delete(class_obj)
            db.commit()
            return {"message": f"Class {class_id} deleted."}
        return {"message": "Class not found."}

    @staticmethod
    def update_class(db: Session, class_id: int, name: str):
        class_obj = db.query(Classes).filter(Classes.id == class_id).first()
        if class_obj:
            class_obj.name = name
            db.commit()
            db.refresh(class_obj)
            return class_obj
        return {"message": "Class not found."}
