@echo off
cd /d G:\obsidian\notes

:: 获取当前日期和时间，作为 commit message
for /f "tokens=1-4 delims=/ " %%i in ('date /t') do (
    set today=%%i-%%j-%%k
)
for /f "tokens=1-2 delims=: " %%i in ('time /t') do (
    set now=%%i-%%j
)

set msg=更新笔记 %today%_%now%

echo.
echo === 拉取远程更新 ===
git pull origin main --no-edit

echo.
echo === 添加文件 ===
git add .

echo.
echo === 提交修改 ===
git commit -m "%msg%"

echo.
echo === 推送到 GitHub ===
git push origin main

echo.
echo ✅ 笔记已同步到 GitHub！
pause
