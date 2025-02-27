from dataclasses import dataclass
from os import getenv
from typing import Dict, Any

from dotenv import load_dotenv, find_dotenv
from src.view import View, FileView, TerminalView

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    api_key: str = str(getenv("API_KEY", default=""))
    api_request_timeout: int = int(getenv("API_REQUEST_TIMEOUT", default=3))
    db_filename: str = getenv("DB_FILENAME", default="currency_operations.db")
    view_filename: str = getenv("VIEW_FILENAME", default="converter_history.csv")


config: Config = Config()

VIEW_CHANNELS_ARGS_MAP: Dict[str, Dict[str, Any]] = {
    "file": {"filename": config.view_filename},
    "terminal": {},
}

VIEW_MAP: Dict[str, View] = {
    "file": FileView(**VIEW_CHANNELS_ARGS_MAP["file"]),
    "terminal": TerminalView(**VIEW_CHANNELS_ARGS_MAP["terminal"]),
}
