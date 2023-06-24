import asyncio
import unittest
from unittest.mock import patch

from fastapi import HTTPException

from main import get


class TestMain(unittest.TestCase):
    def test_get(self) -> None:
        """Test get"""
        url = ""
        with patch('requests.get') as mock:
            asyncio.run(get(url))
            mock.assert_called()

    def test_get_raise_exception(self) -> None:
        """Test get"""
        url = ""
        with self.assertRaises(HTTPException):
            asyncio.run(get(url))


if __name__ == '__main__':
    unittest.main()
