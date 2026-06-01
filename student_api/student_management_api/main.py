from fastapi import FastAPI
from routes.student_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Student Management API"}