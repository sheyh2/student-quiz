from flask import Flask
from src.database.__init__ import db
from app.config import AppConfigs

app = Flask(__name__)

# Config
app.config.from_object(AppConfigs)

# Database
db.init_app(app)


@app.route('/')
def hello():
    return {"say": "Hi"}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
