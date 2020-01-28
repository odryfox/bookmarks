from flask import Flask

from src.web import db


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from src.web import boards
    app.register_blueprint(boards.bp)

    return app
