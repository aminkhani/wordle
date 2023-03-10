from termcolor import colored


def print_success(msg, end=''):
    print(colored(msg, 'green', attrs=["blink"]), end=end)

def print_warning(msg, end='\n'):
    print(colored(msg, 'yellow', attrs=["bold"]), end=end)

def print_error(msg, end='\n'):
    print(colored(msg, 'red', attrs=["bold"]), end=end)

def print_regular(msg, end='\n'):
    print(msg, end=end)
