import os

# Debug what Render is actually passing into the environment variable
raw_url = os.getenv("DATABASE_URL")
print(f"DEBUG - Raw DATABASE_URL from environment: {raw_url!r}")

DATABASE_URL = (raw_url or "").strip()

# Fallback to SQLite if the environment variable is empty or invalid
if not DATABASE_URL or DATABASE_URL.lower() == "none" or DATABASE_URL == "":
    DATABASE_URL = "sqlite:///./urbansense.db"

# Fix Render's postgres:// URL scheme for SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

print(f"DEBUG - Final processed database connection established.")

# Security Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "UrbanSense_AI_Secret_Key_2026_Dev_Only")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
