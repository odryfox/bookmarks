from flask import Flask

from src.web import db


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super_secret_key"
    app.config["FLASK_ADMIN_SWATCH"] = "paper"

    db.init_app(app)

    from src.web import boards
    app.register_blueprint(boards.bp)

    from src.web.admin_panel import admin_panel
    admin_panel.init_app(app)

    return app
