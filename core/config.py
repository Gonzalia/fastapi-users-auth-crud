import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "UsersAuthCrud"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev")

settings = Settings()
