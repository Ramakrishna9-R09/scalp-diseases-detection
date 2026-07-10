@echo off
title ScalpAI — Model Training
color 0A

echo.
echo  ╔══════════════════════════════════════════════╗
echo  ║   🧠 ScalpAI — Model Training Script         ║
echo  ║   Training MobileNetV2 + Custom CNN          ║
echo  ╚══════════════════════════════════════════════╝
echo.
echo  [!] WARNING: Training may take 1-4 hours depending on your hardware.
echo  [!] GPU is strongly recommended for faster training.
echo.

set /p confirm="  Start training? (y/n): "
if /i not "%confirm%"=="y" (
    echo  Training cancelled.
    pause
    exit /b 0
)

echo.
echo  [*] Installing/updating dependencies...
cd /d "%~dp0backend"
pip install -r requirements.txt --quiet

echo  [✓] Dependencies ready
echo.
echo  [*] Starting model training...
echo  [✓] Training logs will appear below
echo  ─────────────────────────────────────────────────
echo.

python train_model.py

echo.
echo  ─────────────────────────────────────────────────
echo  [✓] Training complete! Models saved in backend\models\
echo  You can now run start.bat to launch the application.
echo  ─────────────────────────────────────────────────
pause
