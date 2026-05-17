@echo off
setlocal enabledelayedexpansion

echo ==============================================
echo Character Generation Project Installer
echo ==============================================

echo Checking prerequisites...

REM Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: Git is not installed or not in PATH.
    pause
    exit /b 1
)

REM Check if python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b 1
)

REM Pull or clone the repository
if exist ".git" (
    echo Git repository found. Pulling latest changes...
    git pull
) else (
    if exist "CharacterGeneration\.git" (
        echo Project already cloned.
        cd CharacterGeneration
        echo Pulling latest changes...
        git pull
    ) else (
        echo Cloning repository...
        git clone https://github.com/snorcack/CharacterGeneration.git
        if %ERRORLEVEL% neq 0 (
            echo Error cloning repository.
            pause
            exit /b 1
        )
        cd CharacterGeneration
    )
)

REM Create default .env file
echo.
echo Setting up default environment variables...
if not exist ".env" (
    if exist ".env.example" (
        copy .env.example .env
        echo Created .env from .env.example.
        echo IMPORTANT: Please edit the .env file and add your API keys.
    ) else (
        echo Warning: .env.example not found.
    )
) else (
    echo .env file already exists.
)

REM Setup Backend (Python)
echo.
echo Setting up Python backend...
if exist "CharacterGenerate\backend" (
    cd CharacterGenerate\backend
    echo Creating virtual environment...
    if not exist "venv" (
        python -m venv venv
    )
    echo Activating virtual environment and installing dependencies...
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    call venv\Scripts\deactivate.bat
    cd ..\..
) else (
    echo Warning: Backend folder not found at CharacterGenerate\backend.
)

REM Setup Frontend (Node)
echo.
echo Setting up Node.js frontend...
where npm >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Warning: npm is not installed. Skipping frontend dependencies...
) else (
    if exist "CharacterGenerate\frontend" (
        cd CharacterGenerate\frontend
        echo Installing frontend dependencies...
        call npm install
        cd ..\..
    ) else (
        echo Warning: Frontend folder not found at CharacterGenerate\frontend.
    )
)

echo.
echo ==============================================
echo Installation Complete!
echo ==============================================
echo You may now configure your .env file with your API keys.
echo Run the project using CharacterGenerate\run_app.bat
pause
