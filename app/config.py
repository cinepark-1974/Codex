import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    notion_token: str
    notion_db_id: str
    openai_api_key: str


class ConfigError(ValueError):
    pass


def load_settings() -> Settings:
    notion_token = os.getenv("NOTION_TOKEN", "").strip()
    notion_db_id = os.getenv("NOTION_DB_ID", "").strip()
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()

    missing = [
        name
        for name, value in [
            ("NOTION_TOKEN", notion_token),
            ("NOTION_DB_ID", notion_db_id),
            ("OPENAI_API_KEY", openai_api_key),
        ]
        if not value
    ]
    if missing:
        raise ConfigError(
            "Missing required environment variables: " + ", ".join(missing)
        )

    return Settings(
        notion_token=notion_token,
        notion_db_id=notion_db_id,
        openai_api_key=openai_api_key,
    )
