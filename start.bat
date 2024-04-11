@echo off

echo Skeltah Parser v1.4.4 VENV (Cracked)

pip install requests selenium-driverless colorama psutil
start /B cmd /c "python server.py"
timeout /t 2 /nobreak >nul
start /B cmd /c "python %~dp0dist\start.py"

pause