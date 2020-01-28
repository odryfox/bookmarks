import os

from dotenv import load_dotenv

from src.web import create_app
from src.db import db


load_dotenv()
database_url = os.environ["DATABASE_URL"]
db.init_from_url(database_url)

app = create_app()

if __name__ == "__main__":
    app.run()
