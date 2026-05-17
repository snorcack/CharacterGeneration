@echo off
TITLE Character Portrait Generator - Starting Services...

echo ==========================================================
echo   Character Portrait Generator - Launcher
echo ==========================================================
echo.

:: Get the directory of the batch file
set "BASE_DIR=%~dp0"

:: Read BACKEND_PORT and VITE_PORT from the root .env (one level up from CharacterGenerate/)
set "ENV_FILE=%BASE_DIR%..\\.env"
set "BACKEND_PORT=8000"
set "VITE_PORT=5173"

if exist "%ENV_FILE%" (
    for /f "usebackq tokens=1,* delims==" %%A in ("%ENV_FILE%") do (
        if "%%A"=="BACKEND_PORT" set "BACKEND_PORT=%%B"
        if "%%A"=="VITE_PORT"    set "VITE_PORT=%%B"
    )
)

:: Start Backend
echo [1/2] Starting FastAPI Backend on port %BACKEND_PORT%...
start "Backend (FastAPI)" cmd /c "cd /d "%BASE_DIR%backend" && python main.py"

:: Give backend a moment to start
timeout /t 2 >nul

:: Start Frontend
echo [2/2] Starting React Frontend on port %VITE_PORT%...
echo.
echo Please wait for Vite to initialize.
echo The app will be available at: http://localhost:%VITE_PORT%/
echo.

cd /d "%BASE_DIR%frontend"
npm run dev

pause
