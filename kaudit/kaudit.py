#!/usr/bin/env python3

"""Usage:
  kaudit [--debug] [-V | --verbose]
  kaudit [-h | --help] | [--version]

Options:
  -h --help            show this help message and exit
  --version            show version and exit
  -v --verbose         show extended information
  --debug              enable debugging output (stdout)
"""

import docopt

__version__ = '0.0.1'
__package__ = 'kaudit'
__status__ = 'alpha'
__license__ = 'MIT'
__author__ = u'matthew marchese'
__email__ = 'maffblaster@gentoo.org'
__maintainer__ = u'matthew marchese'
__contributors__ = ''
__copyright__ = '2015-2017'
__description__ = 'a cross-platform desktop screenshot boasting tool'
__url__ = 'https://github.com/digitalsurvival/kaudit'
__source__ = 'https://github.com/digitalsurvival/kaudit'


stager_version = version.get_version()

# Python 3 validator
if sys.version_info < (3, 0):
    print(__name__ + " requires Python 3.0 and up. Exiting...\n")
    sys.exit(1)

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)

    if arguments['--debug'] == True:
        print('Passed arguments:\n' + arguments)
