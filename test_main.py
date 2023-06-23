import asyncio
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from fastapi import HTTPException
from pyngrok.ngrok import NgrokTunnel

from main import close, start_ngrok, get, set_privacy, run_server


class TestMain(unittest.TestCase):
    def test_close(self) -> None:
        """Test close"""
        with patch('main.ngrok.disconnect') as mock, patch('main._connection', return_value=NgrokTunnel):
            close()
            mock.assert_called()

    def test_start_ngrok_when_protocol_is_http(self) -> None:
        """Test start_ngrok with http"""
        protocol = "1"
        self.start_ngrok_base(protocol)

    def test_start_ngrok_when_protocol_is_tcp(self) -> None:
        """Test start_ngrok with tcp"""
        protocol = "1"
        self.start_ngrok_base(protocol)

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

    def start_ngrok_base(self, protocol: str) -> None:
        """Test start_ngrok"""
        out, error = StringIO(), StringIO()
        needle = "Ngrok Public URL"
        connection = NgrokTunnel
        connection.public_url = ""
        with patch.multiple(sys, stdout=out, stderr=error), patch('main.ngrok.connect', return_value=connection):
            start_ngrok("", protocol)
            self.assertTrue(needle in out.getvalue())

    def test_set_privacy_when_input_is_1(self) -> None:
        """Test set_privacy"""
        with patch('main.input', return_value="1") as mock, patch('main.start_ngrok'):
            set_privacy()
            mock.assert_called()

    def test_set_privacy_when_input_is_not_1(self) -> None:
        """Test set_privacy"""
        out, error = StringIO(), StringIO()
        needle = "Private URL : http://localhost:8088"
        with patch.multiple(sys, stdout=out, stderr=error), patch('main.input', return_value="2"), \
                patch('main.start_ngrok'):
            set_privacy()
            self.assertTrue(needle in out.getvalue())

    def test_run_server(self):
        """Test run_server"""
        with patch('uvicorn.run') as mock:
            run_server()
            mock.assert_called()


if __name__ == '__main__':
    unittest.main()
