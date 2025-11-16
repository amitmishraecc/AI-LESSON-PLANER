"""
Run script for AI Lesson Planner
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess

if __name__ == "__main__":
    # Run streamlit app
    subprocess.run(["streamlit", "run", "streamlit.py"])

