from read_args import read_args
from dto import CLIArgs
from greetings import greetings


def main():
    greetings()
    args: CLIArgs = read_args(standalone_mode=False)
    print(args)


if __name__ == '__main__':
    main()
