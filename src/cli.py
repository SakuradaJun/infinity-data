"""
inf

Usage:
  inf init
  inf -h | --help
  inf --version
  inf login
  inf upload <datafile>
  inf install <name==version>

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  inf init
  inf upload data.json
  inf install example.com/people==crawler-1.0.0

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/infamily/infinity-data
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import src.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(src.commands, k) and v:
            module = getattr(src.commands, k)
            src.commands = getmembers(module, isclass)
            command = [command[1] for command in src.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
