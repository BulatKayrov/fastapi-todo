import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH)

    # app
    host: str = "0.0.0.0"
    port: int = 8000

    # database
    echo: bool = False

    @property
    def sqlite_url(self):
        return f"sqlite+aiosqlite:///{BASE_DIR}/database.db"


settings = Settings()
