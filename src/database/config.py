import os


class AppConfig:
    @staticmethod
    def get_db_uri() -> str:
        connection = os.getenv("DB_CONNECTION", "postgres")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_DATABASE")
        user = os.getenv("DB_USERNAME", None)
        password = os.getenv("DB_PASSWORD", None)

        return f"{connection}://{user}:{password}@{host}:{port}/{database}"
