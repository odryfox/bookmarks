from src.db import db


def close_db(response_or_exc):
    db.session.remove()
    return response_or_exc


def init_app(app):
    app.teardown_appcontext(close_db)
