from flask import Blueprint, abort, jsonify

from src.db import db
from src.models import Board
from src.shemas import BoardSchema

bp = Blueprint("boards", __name__, url_prefix="/boards")


@bp.route("")
def index():
    boards = db.session.query(Board).all()
    boards_json = BoardSchema().dump(boards, many=True)

    return jsonify(boards_json)


@bp.route("/<int:board_id>")
def show(board_id: int):
    board = db.session.query(Board).get(board_id)
    if not board:
        abort(404)
    board_json = BoardSchema().dump(board)

    return jsonify(board_json)
