import src.database.config as db_configs


class AppConfigs:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    # default DB
    SQLALCHEMY_DATABASE_URI = db_configs.AppConfig.get_db_uri()

    # connection timeout should be less than wait_timout value in mysql
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True
    }
