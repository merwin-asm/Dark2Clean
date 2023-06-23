import unittest

from tor.interactions import InteractionFactory
from tor.interactions.os import OSInteraction, WindowsInteraction, LinuxInteraction, MacosInteraction


class TestInteractionFactory(unittest.TestCase):
    def test_get_interaction_windows(self):
        interaction: OSInteraction = InteractionFactory.get_interaction('windows')
        self.assertIsInstance(interaction, WindowsInteraction)

    def test_get_interaction_linux(self):
        interaction: OSInteraction = InteractionFactory.get_interaction('linux')
        self.assertIsInstance(interaction, LinuxInteraction)

    def test_get_interaction_macos(self):
        interaction: OSInteraction = InteractionFactory.get_interaction('darwin')
        self.assertIsInstance(interaction, MacosInteraction)

    def test_get_interaction_other(self):
        with self.assertRaises(SystemExit):
            InteractionFactory.get_interaction('other')


if __name__ == '__main__':
    unittest.main()
