# Third party
from termcolor import colored


def warn(message, debug=False):
    """
    Helper function to either print an error, or raise an exception for a full stack trace.
    
    Args:
        message (str): error message to print.
        debug (bool): flag to either thrown an exception, or just print the message. Default: False
    """
    if debug:
        raise Exception(message)  # prints stack trace to console.
    else:
        print(colored(message, "red"))
        raise SystemExit(1)  # does not print trace to console, just exits cli.
