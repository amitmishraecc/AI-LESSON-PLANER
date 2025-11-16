@echo off
echo Creating .env file...
echo.
echo Please enter your Groq API key.
echo You can get it from: https://console.groq.com/
echo.
set /p API_KEY="Enter your Groq API key: "
echo key=%API_KEY% > .env
echo.
echo.
echo MongoDB Setup:
echo Option 1: Use MongoDB Atlas (Cloud) - Enter your connection string
echo Option 2: Use Local MongoDB - Press Enter to skip
echo.
echo MongoDB Atlas connection string format:
echo mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true^&w=majority
echo.
set /p MONGODB_URI="Enter MongoDB URI (or press Enter for localhost): "
if not "%MONGODB_URI%"=="" (
    echo MONGODB_URI=%MONGODB_URI% >> .env
)
echo.
echo .env file created successfully!
echo.
pause

