"""
make test T=test_console
"""
from . import TestInfotech


class TestConsole(TestInfotech):
    """
    console
    """
    def test_console(self):
        """
        console
        """
        from infotech import main, Commands

        self.assertEqual(main([]), 1)
        self.assertEqual(main(['', 'wrong_command', 'wrong_file']), 1)
        self.assertEqual(main(['', Commands.REVERSE, 'wrong_file']), 1)
        self.assertEqual(main(['', Commands.REVERSE, self.fixture('1736.xml')]), 0)
        # self.assertEqual(main(['', Commands.CSV_WELD, self.fixture('1736.xml')]), 0)
        # self.assertEqual(main(['', Commands.CSV_DEFECT, self.fixture('1736.xml')]), 0)
        # self.assertEqual(main(['', Commands.CSV_LINEOBJ, self.fixture('1736.xml')]), 0)
        self.assertEqual(main(['', Commands.REVERSE, self.fixture('1736.xml')]), 0)
        self.assertEqual(main(['', Commands.FIX, self.fixture('1736.xml')]), 0)
        self.assertEqual(main(['', Commands.FIX, self.fixture('umdp-1400.xml')]), 0)
        self.assertEqual(main(['', Commands.JOIN, self.fixture('1736.xml'), '1100', self.fixture('1737.xml')]), 0)

        self.assertEqual(main(['', Commands.MAKEMONEY, self.fixture('1736.xml')]), 0)
        # self.assertEqual(main(['', Commands.CSV_DEFECT, self.fixture('navigation.xml'), True]), 0)
