from read_args import read_args
from dto import CLIArgs
from greetings import greetings
from conversion_value import ObtainingCurrencyQuotes


def main():
    greetings()
    args: CLIArgs = read_args(standalone_mode=False)
    conversion_value: float = ObtainingCurrencyQuotes(
        args.currency_from,
        args.currency_to,
        args.conversion_date
    ).get_conversion_value()

if __name__ == '__main__':
    main()
