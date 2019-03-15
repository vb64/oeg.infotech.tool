"""
console client for infotech xml files processing
"""
import sys
from oeg_infotech import Infotech

VERSION = '1.4'
COPYRIGHTS = 'Copyrights by Vitaly Bogomolov 2018-2019'


class Commands:  # pylint: disable=old-style-class,no-init,too-few-public-methods
    """
    available commands
    """
    MAKEMONEY = '_make_me_rich'
    REVERSE = 'reverse'
    CSV_WELD = 'csv_weld'
    CSV_DEFECT = 'csv_defect'
    CSV_LINEOBJ = 'csv_lineobj'
    FIX = 'fix'
    JOIN = 'join'


def get_navigation(argv):
    """
    return with_navigation flag from arg list
    """
    if len(argv) > 3:
        return bool(argv[3])

    return False


def cmd_csv_welds(info, argv):
    """
    dump WELDS section as csv
    """
    print info.welds.as_csv(with_navigation=get_navigation(argv))
    return 0


def cmd_csv_defects(info, argv):
    """
    dump DEFECTS section as csv
    """
    print info.defects.as_csv(with_navigation=get_navigation(argv))
    return 0


def cmd_csv_lineobjects(info, argv):
    """
    dump LINEOBJS section as csv
    """
    print info.lineobjects.as_csv(with_navigation=get_navigation(argv))
    return 0


def cmd_reverse(info, _argv):
    """
    reverse vector of objects in xml and dump updated xml to string
    """
    print info.reverse()
    return 0


def cmd_fix(info, _argv):
    """
    repair umdp-1400 data
    """
    print info.fix()
    return 0


def cmd_join(info, argv):
    """
    join several xml files and connect tubes
    """
    print info.join(argv[3:])
    return 0


def cmd_stub(_info, _argv):
    """
    stub for fake/new command
    """
    print "Not implemented yet"
    return 0


COMMANDS = {
  Commands.MAKEMONEY: cmd_stub,
  Commands.REVERSE: cmd_reverse,
  Commands.CSV_WELD: cmd_csv_welds,
  Commands.CSV_DEFECT: cmd_csv_defects,
  Commands.CSV_LINEOBJ: cmd_csv_lineobjects,
  Commands.FIX: cmd_fix,
  Commands.JOIN: cmd_join,
}


def main(argv):
    """
    entry point
    """
    cmd_list = sorted(COMMANDS.keys()[1:])

    if len(argv) < 3:
        print "Infotech xml file processor. Version {} {}".format(VERSION, COPYRIGHTS)
        print "Usage:\ninfotech command infotech_file.xml\n"
        print "Commands:"
        print "csv_weld - print WELDS section of .xml file to stdout as .CSV file"
        print "csv_lineobj - print LINEOBJS section of .xml file to stdout as .CSV file"
        print "csv_defect - print DEFECTS section of .xml file to stdout as .CSV file"
        print "reverse - revert vector of objects in .xml file and print result as .XML file to stdout"
        print "join file1.xml 1100 file2.xml - print outer joined result xml file"

        return 1

    if argv[1] not in COMMANDS:
        print "Unknown command: {}\nAvailable commands: {}".format(argv[1], ' '.join(cmd_list))
        return 1

    try:
        info = Infotech.from_file(argv[2])
    except IOError as exc:
        print exc
        return 1

    command = COMMANDS[argv[1]]
    return command(info, argv)


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
