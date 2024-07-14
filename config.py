import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max-limit