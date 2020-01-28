from flask import Blueprint, jsonify

from src.db import db
from src.models import Board

bp = Blueprint("boards", __name__, url_prefix="/boards")


@bp.route("/")
def index():
    boards = db.session.query(Board).all()
    boards_json = list(map(lambda board: {"id": board.id}, boards))
    return jsonify(boards_json)
