from flask import Flask

from src.web import db


def create_app(env_name):
    app = Flask(__name__)

    from src.web.config import config_by_env_name
    app.config.from_object(config_by_env_name[env_name])

    db.init_app(app)

    from src.web import boards
    app.register_blueprint(boards.bp)

    from src.web.admin_panel import admin_panel
    admin_panel.init_app(app)

    return app
