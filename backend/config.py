import os

# Database Configuration
# Change this line in backend/config.py:
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./urbansense.db"

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
# Security Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "UrbanSense_AI_Secret_Key_2026_Dev_Only")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
