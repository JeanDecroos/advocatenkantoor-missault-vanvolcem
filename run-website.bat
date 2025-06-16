@echo off
title Advocatenkantoor Missault - Van Volcem Website Server

echo.
echo ========================================================
echo    Advocatenkantoor Missault - Van Volcem Website
echo ========================================================
echo.

REM Controleer of Python beschikbaar is
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is niet geinstalleerd of niet gevonden in PATH
    echo.
    echo 💡 Installeer Python van https://python.org
    echo    Zorg ervoor dat Python wordt toegevoegd aan PATH
    echo.
    pause
    exit /b 1
)

REM Controleer of bestanden bestaan
if not exist "index.html" (
    echo ❌ index.html niet gevonden
    goto :missing_files
)
if not exist "styles.css" (
    echo ❌ styles.css niet gevonden
    goto :missing_files
)
if not exist "script.js" (
    echo ❌ script.js niet gevonden
    goto :missing_files
)

echo ✅ Alle bestanden gevonden!
echo.
echo 🚀 Website server wordt gestart...
echo 💡 De website opent automatisch in je browser
echo 🛑 Druk Ctrl+C om de server te stoppen
echo.

REM Start Python server
if exist "run-server.py" (
    python run-server.py
) else (
    echo 📡 Start eenvoudige HTTP server...
    python -m http.server 8000
)

goto :end

:missing_files
echo.
echo ❌ Benodigde website bestanden ontbreken!
echo    Zorg ervoor dat alle bestanden in dezelfde map staan:
echo    - index.html
echo    - styles.css  
echo    - script.js
echo.
pause
exit /b 1

:end
echo.
echo ✅ Server afgesloten
pause 