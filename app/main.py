from flask import Flask
from src.database.__init__ import db
from app.config import AppConfigs
from app.api.routes.__init__ import BaseRoutes
from app.api.middlewares.auth import Authenticate

app = Flask(__name__)
app.wsgi_app.add = Authenticate(app.wsgi_app)

# Config
app.config.from_object(AppConfigs)

# Database
db.init_app(app)

# Routes
base_routes = BaseRoutes(app)
base_routes.init_routes()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
