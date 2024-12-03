# app/models/classes.py
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base

class Classes(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    students = relationship("Students", back_populates="class_")

    def __repr__(self):
        return f"<Classes(name={self.name}, start_date={self.start_date})>"
