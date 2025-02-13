from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from os import getenv

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    api_key: str = getenv("API_KEY")


config: Config = Config()
