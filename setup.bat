@echo off
echo 🔧 Setting up Python virtual environment...
python -m venv venv

if exist venv\Scripts\activate (
    call venv\Scripts\activate
    echo 📦 Installing dependencies from requirements.txt...
    pip install --upgrade pip
    pip install -r requirements.txt

    echo ✅ Setup complete.
    echo To activate the environment later, run: venv\Scripts\activate
) else (
    echo ❌ Failed to create virtual environment. Check if Python is installed and added to PATH.
)

pause
