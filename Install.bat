@echo off

echo Installing pywin32...
pip install pywin32 > nul

if %errorlevel% NEQ 0 (
    echo Failed to install pywin32. Please check the error message above.
) else (
    echo pywin32 installed successfully.
)

pause
exit
