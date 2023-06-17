import sys
import unittest
from io import StringIO
from unittest.mock import patch
from main import start_tor


class TestMain(unittest.TestCase):
    def test_start_tor_windows(self) -> None:
        """Test start_tor"""
        self.start_tor_base('windows')

    def test_start_tor_linux(self) -> None:
        """Test start_tor"""
        self.start_tor_base('linux')

    def test_start_tor_mac(self) -> None:
        """Test start_tor"""
        self.start_tor_base('darwin')

    def test_start_tor_other(self) -> None:
        """Test start_tor"""
        out, error = StringIO(), StringIO()
        os = 'android'

        with patch('subprocess.run'), patch.multiple(sys, stdout=out, stderr=error, platform=os), \
                self.assertRaises(SystemExit):
            start_tor()

    def start_tor_base(self, os: str) -> None:
        out, error = StringIO(), StringIO()
        needle = "Tor service restarted successfully"

        with patch('subprocess.run'), patch.multiple(sys, stdout=out, stderr=error, platform=os):
            start_tor()

        result = needle in out.getvalue()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
