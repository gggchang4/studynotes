@echo off
chcp 65001 >nul

:: Change directory to your notes repository
cd /d G:\obsidian\notes

:: --- Get current date and time (safe for any locale) ---
for /f "tokens=2 delims==." %%i in ('"wmic os get localdatetime /value"') do set datetime=%%i

:: datetime looks like: 20251112004236.000000+480
:: Extract date components
set yy=%datetime:~2,2%
set mm=%datetime:~4,2%
set dd=%datetime:~6,2%

:: Generate commit message
set msg=study note update in %yy%/%mm%/%dd%

echo.
echo === Pulling from remote repository ===
git pull origin main --no-edit
if errorlevel 1 (
    echo [ERROR] Git pull failed.
    pause
    exit /b
)

echo.
echo === Adding files ===
git add .

echo.
echo === Committing changes ===
git diff --quiet
if %errorlevel% equ 0 (
    echo No changes detected, skipping commit.
) else (
    git commit -m "%msg%"
    echo.
    echo === Pushing to GitHub ===
    git push origin main
)

echo.
echo Notes have been successfully synced to GitHub.
pause
