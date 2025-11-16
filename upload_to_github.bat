@echo off
echo ========================================
echo AI Lesson Planner - GitHub Upload Script
echo ========================================
echo.

REM Check if git is initialized
if not exist .git (
    echo Initializing git repository...
    git init
    echo Git repository initialized!
    echo.
)

REM Check if .env exists and warn
if exist .env (
    echo [WARNING] .env file detected. Make sure it's in .gitignore!
    echo Checking .gitignore...
    findstr /C:".env" .gitignore >nul
    if errorlevel 1 (
        echo [ERROR] .env is NOT in .gitignore! Please add it before proceeding.
        pause
        exit /b 1
    ) else (
        echo [OK] .env is properly ignored.
    )
    echo.
)

echo Adding all files to git...
git add .

echo.
echo Current status:
git status --short

echo.
echo ========================================
echo Ready to commit!
echo ========================================
echo.
echo Next steps:
echo 1. Review the files above
echo 2. Run: git commit -m "Initial commit: Production-ready AI Lesson Planner"
echo 3. Create repository on GitHub: https://github.com/new
echo 4. Run: git remote add origin https://github.com/YOUR_USERNAME/ai-lesson-planner.git
echo 5. Run: git branch -M main
echo 6. Run: git push -u origin main
echo.
echo For detailed instructions, see: docs\GITHUB_SETUP.md
echo.
pause

