from flask_sqlalchemy import SQLAlchemy


class Database(SQLAlchemy):
    def init_app(self, app) -> None:
        super().init_app(app)


db = Database()
