import os
from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT = os.getenv("TEST_ENV", "local")

BASE_URLS = {
    "local": "http://127.0.0.1:8000"
}

BASE_URL = BASE_URLS.get(ENVIRONMENT)

if not BASE_URL:
    raise ValueError(
        f"Unsupported test environment: {ENVIRONMENT}"
    )


DATABASE_PATH = os.getenv(
    "TRIPMATE_DB_PATH",
    "tripmate.db"
)