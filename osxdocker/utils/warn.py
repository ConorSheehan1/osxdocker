# Third party
from termcolor import colored


def warn(message, debug=False):
    if debug:
        raise Exception(message)  # prints stack trace to console.
    else:
        print(colored(message, "red"))
        raise SystemExit(1)  # does not print trace to console, just exits cli.
