@echo off
title ScalpAI — Scalp Disease Detection
color 0B

echo.
echo  ╔══════════════════════════════════════════════╗
echo  ║   🔬 ScalpAI — Scalp Disease Detection       ║
echo  ║   Powered by MobileNetV2 + CNN               ║
echo  ╚══════════════════════════════════════════════╝
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python is not installed or not in PATH.
    echo  Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo  [✓] Python found
echo.

:: Install requirements
echo  [*] Installing Python dependencies...
cd /d "%~dp0backend"
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo  [WARNING] Some packages may have failed to install.
)
echo  [✓] Dependencies ready
echo.

:: Create models directory
if not exist "models" mkdir models
echo  [✓] Models directory ready
echo.

:: Check if models exist
if exist "models\cnn_model.h5" (
    echo  [✓] CNN model found
) else (
    echo  [!] CNN model NOT found — running in Demo/Simulation mode
)
if exist "models\mobilenet_model.h5" (
    echo  [✓] MobileNetV2 model found
) else (
    echo  [!] MobileNetV2 model NOT found — running in Demo/Simulation mode
)
echo.

:: Open frontend in browser
echo  [*] Opening frontend in browser...
start http://localhost:5000

echo.
echo  [*] Starting Flask API server...
echo  [✓] API will be available at: http://localhost:5000
echo.
echo  ─────────────────────────────────────────────────
echo   Press Ctrl+C to stop the server
echo  ─────────────────────────────────────────────────
echo.

python app.py

pause
