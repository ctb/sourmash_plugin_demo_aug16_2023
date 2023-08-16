"""xyz plugin description HI BRY"""

usage="""
   sourmash scripts xyz
"""

epilog="""
See https://github.com/xyz for more examples.

Need help? Have questions? Ask at http://github.com/sourmash/issues!
"""

import argparse
import sourmash

from sourmash.index import LinearIndex
from sourmash.logging import debug_literal
from sourmash.plugins import CommandLinePlugin

from sourmash.save_load import (Base_SaveSignaturesToLocation,
                                _get_signatures_from_rust)


###

#
# CLI plugin - supports 'sourmash scripts xyz'
#

class Command_XYZ(CommandLinePlugin):
    command = 'yo-annie'             # 'scripts <command>'
    description = __doc__       # output with -h
    usage = usage               # output with no args/bad args as well as -h
    epilog = epilog             # output with -h
    formatter_class = argparse.RawTextHelpFormatter # do not reformat multiline

    def __init__(self, subparser):
        super().__init__(subparser)
        # add argparse arguments here.
        debug_literal('RUNNING cmd_xyz.__init__')
        subparser.add_argument('colton', help='colton wuz here')
        subparser.add_argument('-H', '--hazel', required=True)
        subparser.add_argument('--no-save', action='store_true', help='discard all results without doing anything')

    def main(self, args):
        # code that we actually run.
        super().main(args)
        print('RUNNING cmd', self, args)
