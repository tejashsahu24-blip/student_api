from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.student import Student
from models.student_schema import StudentCreate

router = APIRouter()

# CREATE
@router.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# READ ALL
@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# READ ONE
@router.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.id == id).first()


# UPDATE
@router.put("/students/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    data = db.query(Student).filter(Student.id == id).first()

    if data:
        data.name = student.name
        data.age = student.age
        data.course = student.course

        db.commit()
        db.refresh(data)

    return data


# DELETE
@router.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):

    student = db.query(Student).filter(Student.id == id).first()

    if student:
        db.delete(student)
        db.commit()

    return {"message": "Student deleted successfully"}