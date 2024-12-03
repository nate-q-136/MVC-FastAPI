# app/models/students.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    class_id = Column(Integer, ForeignKey("classes.id"))  # Khóa ngoại đến bảng Classes
    class_ = relationship("Classes", back_populates="students")

    def __repr__(self) -> str:
        return f"<Students(name={self.full_name})>"
