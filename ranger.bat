@echo off
chcp 65001 >nul
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    py ranger.py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python ranger.py
    ) else (
        echo Python n'est pas installe ou pas dans le PATH.
        echo Telecharge-le sur https://www.python.org/downloads/
    )
)

echo.
pause
