"""Configuration management for the Analyst Bot."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

    # Gemini AI
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # Database
    DATABASE_URL = os.getenv('DATABASE_URL')

    # Bot Settings
    ADMIN_USER_IDS = os.getenv('ADMIN_USER_IDS', '').split(',')

    @classmethod
    def validate(cls):
        """Validate that all required config values are set."""
        missing = []

        if not cls.TELEGRAM_BOT_TOKEN:
            missing.append('TELEGRAM_BOT_TOKEN')
        if not cls.GEMINI_API_KEY:
            missing.append('GEMINI_API_KEY')
        if not cls.DATABASE_URL:
            missing.append('DATABASE_URL')

        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        return True
