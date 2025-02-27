from src.greetings import greetings
from src.read_args import read_args
from src.dto import CLIArgs
from src.logic import Logic
from src.config import config, VIEW_MAP
from src.db import Storage

if __name__ == '__main__':
    greetings()
    args: CLIArgs = read_args(standalone_mode=False)

    Logic(
        storage=Storage(config.db_filename),
        views_map=VIEW_MAP
    ).run(args=args)
