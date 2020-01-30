import os

from dotenv import load_dotenv

from src.web import create_app
from src.db import db


load_dotenv()
database_url = os.environ["DATABASE_URL"]
db.init_from_url(database_url)

env_name = os.environ.get("ENV_NAME", "prod")
app = create_app(env_name)

if __name__ == "__main__":
    app.run()
