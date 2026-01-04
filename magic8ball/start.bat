@echo off
REM Magic 8 Ball - Startup Script for Windows

echo.
echo 🎱 Magic 8 Ball - Startup
echo ========================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo ✨ Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt -q

REM Run tests
echo 🧪 Running tests...
pytest tests/ -v --tb=short

REM Start the server
echo.
echo 🚀 Starting Magic 8 Ball server...
echo    📍 URL: http://localhost:8000
echo    🛑 Press Ctrl+C to stop
echo.

python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
pause
