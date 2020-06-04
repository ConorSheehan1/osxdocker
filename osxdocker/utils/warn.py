# Third party
from termcolor import colored


def warn(message: str, debug: bool = False):
    """
    Helper function to either print an error, or raise an exception for a full stack trace.

    Args:
        message: error message to print.
        debug: flag to either thrown an exception, or print the message and exit. Default: False

    Raises:
        Exception: if debug is True, to provide a full trace
        SystemExit: if debug is False, to return a non-zero status indicating the original command failed
    """
    if debug:
        raise Exception(message)  # prints stack trace to console.
    else:
        print(colored(message, "red"))
        raise SystemExit(1)  # does not print trace to console, just exits cli.
