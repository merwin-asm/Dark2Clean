import unittest

from converters.option_to_protocol_converter import OptionToProtocolConverter


class MyTestCase(unittest.TestCase):
    def test_convert_when_option_is_2(self):
        converted = OptionToProtocolConverter.convert("2")
        self.assertEqual("http", converted)

    def test_convert_when_option_is_not_2(self):
        converted = OptionToProtocolConverter.convert("1")
        self.assertEqual("https", converted)


if __name__ == '__main__':
    unittest.main()
