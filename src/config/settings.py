"""
Application settings and configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    
    # MongoDB Settings
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = "StudentDB"
    COLLECTION_USERS = "users"
    COLLECTION_PLANS = "lesson_plans"
    
    # API Settings
    GROQ_API_KEY = os.getenv('key')
    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_TEMPERATURE = 0.7
    
    # App Settings
    APP_NAME = "AI Lesson Planner"
    APP_VERSION = "2.0.0"
    
    # Social Links
    LINKEDIN_URL = "https://www.linkedin.com/in/mishraamitjnp/"
    GITHUB_URL = "https://github.com/amitmishraecc"
    EMAIL = "mishraamit7348@gmail.com"
    PORTFOLIO_URL = "https://basic-portfolio-xi.vercel.app/"
    
    @classmethod
    def validate(cls):
        """Validate required settings"""
        if not cls.GROQ_API_KEY or cls.GROQ_API_KEY == 'your_groq_api_key_here':
            raise ValueError("Groq API key not configured. Please set 'key' in .env file")

