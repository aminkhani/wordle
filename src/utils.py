"""Utility of the game.
Use the termcolor library.
This library alow us to hava a colorfull output on terminal.
for more information about the libarary: Site Link
"""
from termcolor import colored


def print_success(msg: str, end=''):
    """
    Output on terminal will be green and blink.
    """

    print(colored(msg, 'green', attrs=["blink"]), end=end)

def print_warning(msg: str, end='\n'):
    """
    Output on terminal will be yellow and bold.
    """

    print(colored(msg, 'yellow', attrs=["bold"]), end=end)

def print_error(msg: str, end='\n'):
    """
    Output on terminal will be red and bold.
    """

    print(colored(msg, 'red', attrs=["bold"]), end=end)

def print_regular(msg: str, end='\n'):
    """
    Simple output, don't used the library.
    """

    print(msg, end=end)
