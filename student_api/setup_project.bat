@echo off
echo Creating Student Management API project structure...

:: Create folders
mkdir student_management_api
cd student_management_api

mkdir models
mkdir routes
mkdir database

:: Create files
type nul > main.py
type nul > models\student.py
type nul > routes\student_routes.py
type nul > database\db.py
type nul > requirements.txt
type nul > README.md

echo.
echo Project structure created successfully!
pause