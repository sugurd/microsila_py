"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mmicrosila_py` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``microsila_py.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``microsila_py.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys

import microsila_py


def print_package_version():
    print(f"microsila_py version {microsila_py.__version__}")


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    total = len(argv)
    if not total:
        return 0
    if total == 1:
        print_package_version()
        return 0

    if argv[1] == '--version':
        print_package_version()
    elif argv[1] == '--help':
        print(f"microsila_py is a python backend for MCU development library")
    else:
        print(f"Unknown command, try '--help'")
    return 0
