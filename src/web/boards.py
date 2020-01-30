from flask import Blueprint, jsonify

from src.db import db
from src.models import Board
from src.shemas import BoardSchema

bp = Blueprint("boards", __name__, url_prefix="/boards")


@bp.route("/")
def index():
    boards = db.session.query(Board).all()
    boards_json = BoardSchema().dump(boards, many=True)

    return jsonify(boards_json)
