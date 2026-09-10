import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

TRIPMATE_PATH = os.path.join(
    os.path.dirname(BASE_DIR),
    "tripmate"
)

DATABASE_PATH = os.path.join(
    TRIPMATE_PATH,
    "tripmate.db"
)

ENVIRONMENT = os.getenv("TEST_ENV", "local")

BASE_URLS = {
    "local": "http://127.0.0.1:8000"
}

BASE_URL = BASE_URLS.get(ENVIRONMENT)

if not BASE_URL:
    raise ValueError(
        f"Unsupported test environment: {ENVIRONMENT}"
    )