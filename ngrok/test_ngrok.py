import sys
import unittest
from io import StringIO
from unittest.mock import patch

from .ngrok import Ngrok


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ngrok = Ngrok()

    def test_close(self) -> None:
        """Test close"""
        with patch('pyngrok.ngrok.disconnect') as mock:
            self.ngrok.close()
            mock.assert_not_called()

    def test_set_privacy_when_input_is_1(self):
        out, error = StringIO(), StringIO()
        needle = 'Ngrok Public URL'
        with patch.multiple(sys, stdout=out, stderr=error), patch('builtins.input', return_value='1'), \
                patch('ngrok.ngrok.ngrok.connect'):
            self.ngrok.set_privacy()
            self.assertTrue(needle in out.getvalue())

    def test_set_privacy_when_input_is_2(self):
        needle = 'Private URL'
        out, error = StringIO(), StringIO()
        with patch.multiple(sys, stdout=out, stderr=error), patch('builtins.input', return_value='2'):
            self.ngrok.set_privacy()
            self.assertTrue(needle in out.getvalue())

    def test_start(self):
        needle = 'Ngrok Public URL'
        out, error = StringIO(), StringIO()
        with patch.multiple(sys, stdout=out, stderr=error), patch('ngrok.ngrok.ngrok.connect'):
            self.ngrok.start('', '1')
            self.assertTrue(needle in out.getvalue())

    def test_run(self):
        needle = 'uses port 8088'
        out, error = StringIO(), StringIO()
        with patch.multiple(sys, stdout=out, stderr=error), patch('uvicorn.run'):
            self.ngrok.run()
            self.assertTrue(needle in out.getvalue())


if __name__ == '__main__':
    unittest.main()
