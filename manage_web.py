import os

from dotenv import load_dotenv

from src.config import config
from src.web import create_app
from src.db import db


load_dotenv()
env_name = os.environ.get("ENV_NAME", "prod")

config.init_from_env_name(env_name)
db.init_from_url(config.DATABASE_URL)

app = create_app(env_name)

if __name__ == "__main__":
    app.run()
