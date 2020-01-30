from flask import Blueprint, jsonify

from src.db import db
from src.models import Board

bp = Blueprint("boards", __name__, url_prefix="/boards")


@bp.route("/")
def index():
    boards = db.session.query(Board).all()

    def to_json(board: Board) -> dict:
        return {"id": board.id, "name": board.name}

    boards_json = list(map(to_json, boards))
    return jsonify(boards_json)
