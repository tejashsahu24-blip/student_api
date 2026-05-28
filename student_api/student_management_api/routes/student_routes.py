from fastapi import APIRouter
from database.db import SessionLocal
from models.student_model import Student

router = APIRouter()

# Create DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 👉 GET all students
@router.get("/students")
def get_students():
    db = next(get_db())
    students = db.query(Student).all()
    return students


# 👉 ADD student
@router.post("/students")
def add_student(name: str, age: int):
    db = next(get_db())
    new_student = Student(name=name, age=age)
    db.add(new_student)
    db.commit()
    return {"message": "Student added"}


# 👉 DELETE student
@router.delete("/students/{id}")
def delete_student(id: int):
    db = next(get_db())
    student = db.query(Student).filter(Student.id == id).first()
    
    if not student:
        return {"error": "Student not found"}
    
    db.delete(student)
    db.commit()
    return {"message": "Deleted"}