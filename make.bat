@echo off

rem Command to start the development server
if "%1"=="runserver" (
    call .\project.\venv\Scripts\activate.bat
    cd .\project
    py manage.py runserver
)

rem Command to apply migrations
if "%1"=="migrate" (
    call .\project.\venv\Scripts\activate.bat
    cd .\project
    py manage.py migrate
)

rem Command to lint files with flake8
if "%1"=="lint" (
    call .\project\venv\Scripts\activate.bat
    cd .\project\sweetsky
    for %%f in (*.py) do (
        flake8 --config=.flake8 "%%f"
        black "%%f"
    )
)

rem Command Activate venv
if "%1"=="activate" (
    call .\project\venv\Scripts\activate.bat
)

rem Command deactivate venv
if "%1"=="deactivate" (
    call .\project.\venv\Scripts\deactivate.bat
)