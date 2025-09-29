@echo off
chcp 65001 >nul  :: use UTF-8 to avoid encoding issues

cd /d G:\obsidian\notes

:: get current date (yyyy-MM-dd) and time (HH-mm)
for /f "tokens=1-4 delims=/ " %%i in ('date /t') do (
    set today=%%i-%%j-%%k
)
for /f "tokens=1-2 delims=: " %%i in ('time /t') do (
    set now=%%i-%%j
)

set msg=update_notes_%today%_%now%

echo.
echo === Pull from remote ===
git pull origin main --no-edit

echo.
echo === Add files ===
git add .

echo.
echo === Commit changes ===
git commit -m "%msg%"

echo.
echo === Push to GitHub ===
git push origin main

echo.
echo Notes synced to GitHub successfully.
pause
