@echo off
echo ===============================
echo Installing requirements...
echo ===============================
pip install -r requirements.txt

echo ===============================
echo Launching Auto-py-to-apk GUI...
echo ===============================
auto-py-to-apk

echo ===============================
echo Done! Press any key to exit.
echo ===============================
pause
