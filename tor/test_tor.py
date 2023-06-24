import sys
import unittest
from io import StringIO
from unittest.mock import patch

from requests import Response

from tor import Tor


class TestTor(unittest.TestCase):
    def setUp(self) -> None:
        self.tor: Tor = Tor()
        self.response: Response = Response()
        self.response._content = ''.encode()

    def test_is_installed_when_tor_is_installed(self):
        """Test is_installed"""
        with patch('subprocess.check_output'):
            self.assertTrue(self.tor.is_installed())

    def test_is_installed_when_tor_is_not_installed(self):
        """Test is_installed"""
        with patch('subprocess.check_output', side_effect=OSError):
            self.assertFalse(self.tor.is_installed())

    def test_install_when_is_installed(self) -> None:
        """Test install"""
        out, error = StringIO(), StringIO()
        needle = "Checking if Tor installed"

        with patch('subprocess.check_output'), patch.multiple(sys, stdout=out, stderr=error):
            self.tor.install()
            self.assertTrue(needle in out.getvalue())

    def test_install_when_is_not_installed(self) -> None:
        """Test install"""
        out, error = StringIO(), StringIO()
        self.response._content = '<a class="downloadLink" href="dist/torbrowser/12.5/torbrowser-install-win64-12.5' \
                                 '_ALL.exe">Download for Windows</a>'.encode()

        with patch('subprocess.check_output', side_effect=OSError) as mock, \
                patch('requests.get', return_value=self.response), patch('subprocess.run'), patch('os.remove'), \
                patch.multiple(sys, stdout=out, stderr=error):
            self.tor.install()
            mock.assert_called()

    def test_install_when_is_not_installed_and_is_not_download_link(self) -> None:
        """Test install"""
        out, error = StringIO(), StringIO()

        with patch('subprocess.check_output', side_effect=OSError) as mock, \
                patch('requests.get', return_value=self.response), patch('subprocess.run'), patch('os.remove'), \
                patch.multiple(sys, stdout=out, stderr=error), self.assertRaises(SystemExit):
            self.tor.install()

    def test_install_when_raises_an_exception(self) -> None:
        """Test install"""
        out, error = StringIO(), StringIO()

        with patch('subprocess.check_output', side_effect=OSError), patch('sys.platform', return_value='win32'), \
                patch('requests.get', side_efect=SystemExit), patch.multiple(sys, stdout=out, stderr=error), \
                self.assertRaises(SystemExit):
            self.tor.install()

    def test_start(self):
        """Test start"""
        with patch('subprocess.run') as mock:
            self.tor.start()
            mock.assert_called()


if __name__ == '__main__':
    unittest.main()
