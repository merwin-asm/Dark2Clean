import unittest
from unittest.mock import patch

from interactions.os import OSInteraction, WindowsInteraction


class TestWindows(unittest.TestCase):
    def setUp(self) -> None:
        self.interaction: OSInteraction = WindowsInteraction()

    def test_start(self) -> None:
        with patch('subprocess.run') as mock:
            self.interaction.start()
            mock.assert_called()

    def test_install(self) -> None:
        with patch('subprocess.run') as mock, patch('requests.get'):
            self.interaction.start()
            mock.assert_called()


if __name__ == '__main__':
    unittest.main()
