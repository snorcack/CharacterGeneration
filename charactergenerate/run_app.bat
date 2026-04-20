@echo off
TITLE Character Portrait Generator - Starting Services...

echo ==========================================================
echo   Character Portrait Generator - Launcher
echo ==========================================================
echo.

:: Get the directory of the batch file
set "BASE_DIR=%~dp0"

:: Start Backend
echo [1/2] Starting FastAPI Backend on port 8000...
start "Backend (FastAPI)" cmd /c "cd /d "%BASE_DIR%backend" && python main.py"

:: Give backend a moment to start
timeout /t 2 >nul

:: Start Frontend
echo [2/2] Starting React Frontend on port 5173...
echo.
echo Please wait for Vite to initialize.
echo The app will be available at: http://localhost:5173/
echo.

cd /d "%BASE_DIR%frontend"
npm run dev

pause
