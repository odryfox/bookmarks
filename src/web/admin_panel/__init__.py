from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from src.db import db
from src.models import Board

admin_panel = Admin(name="Bookmarks dashboard", template_mode="bootstrap3")
admin_panel.add_view(ModelView(Board, db.session))
