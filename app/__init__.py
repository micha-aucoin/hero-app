from os import getenv

from dotenv import load_dotenv

from app.core.config import Settings

if getenv('ENV_FILE'):
    load_dotenv(getenv("ENV_FILE"))

else:
    getenv("API_V1_PREFIX")
    getenv("DEBUG")
    getenv("PROJECT_NAME")
    getenv("VERSION")
    getenv("DESCRIPTION")
    getenv("DB_ASYNC_CONNECTION_STR")
    getenv("DB_ASYNC_TEST_CONNECTION_STR")
    getenv("DB_EXCLUDE_TABLES")

settings = Settings()
