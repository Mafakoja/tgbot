import os
from dataclasses import dataclass

@dataclass
class Settings:
    token: str = os.getenv("BOT_TOKEN", "")
    db_path: str = os.getenv("DB_PATH", "bot.db")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "admin")

settings = Settings()
