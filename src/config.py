from dataclasses import dataclass
from os import getenv
from typing import Dict, Type, Any

from dotenv import load_dotenv, find_dotenv
from src.view import View, FileView, TerminalView
from src.db import Storage

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    api_key: str = str(getenv("API_KEY", default=""))
    api_request_timeout: int = int(getenv("API_REQUEST_TIMEOUT", default=3))
    db_name: Storage = Storage("currency_operations.db")


config: Config = Config()

VIEW_CHANNELS_MAP: Dict[str, Type[View]] = {
    "file": FileView,
    "terminal": TerminalView,
}

VIEW_CHANNELS_ARGS_MAP: Dict[str, Dict[str, Any]] = {
    "file": {"filename": "converter_history.csv"},
    "terminal": {},
}
