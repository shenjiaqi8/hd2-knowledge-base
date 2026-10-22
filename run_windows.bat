@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 scripts\update_repo.py %*
) else (
    python scripts\update_repo.py %*
)
if errorlevel 1 (
    echo.
    echo Update FAILED. Check the error above.
) else (
    echo.
    echo Update finished.
)
pause
