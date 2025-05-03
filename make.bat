@echo off

rem Command to start the development server
if "%1"=="runserver" (
    call .\venv\Scripts\activate.bat
    cd .\todo_app
    py manage.py runserver
)

rem Command to apply migrations
if "%1"=="migrate" (
    call .\venv\Scripts\activate.bat
    cd .\todo_app
    py manage.py migrate
)

rem Command to lint files with flake8
if "%1"=="lint" (
    call .\venv\Scripts\activate.bat
    cd .\todo_app\tasks
    for %%f in (*.py) do (
        flake8 --config=.flake8 "%%f"
        black "%%f"
    )
)

rem Command Activate venv
if "%1"=="activate" (
    call .\venv\Scripts\activate.bat
)

rem Command deactivate venv
if "%1"=="deactivate" (
    call .\venv\Scripts\deactivate.bat
)