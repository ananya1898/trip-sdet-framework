import os
from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT = os.getenv("TEST_ENV", "local")

BASE_URLS = {
    "local": os.getenv("LOCAL_BASE_URL"),
    "qa": os.getenv("QA_BASE_URL"),
}

BASE_URL = BASE_URLS.get(ENVIRONMENT)

if not BASE_URL:
    raise ValueError(
        f"BASE_URL is not configured for environment: {ENVIRONMENT}"
    )


DATABASE_PATH = os.getenv(
    "TRIPMATE_DB_PATH"
)

if not DATABASE_PATH:
    raise ValueError(
        "TRIPMATE_DB_PATH is not configured"
    )