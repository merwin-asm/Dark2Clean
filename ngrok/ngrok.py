import atexit

import uvicorn
from fastapi import FastAPI
from pyngrok import ngrok

from converters import OptionToProtocolConverter

app = FastAPI()


class Ngrok:
    def __init__(self):
        self._connection = None

    def close(self):
        if self._connection is not None:
            ngrok.disconnect(self._connection.public_url)

    def set_privacy(self):
        if input("Public or Private (1/2): ") == "1":
            self.start(input("Ngrok Auth : "), input("1 Http or 2 Https (note using https "
                                                     "can get 'your ip expossed') : "))
        else:
            print(f"\n[bold][dark_orange]Private URL : http://localhost:8088[/dark_orange][/bold]\n\n")

    def start(self, auth, protocol_option):
        ngrok.set_auth_token(auth)
        protocol = OptionToProtocolConverter.convert(protocol_option)
        self._connection = ngrok.connect(8088, protocol)
        print(f"\n[bold][dark_orange]Ngrok Public URL : {self._connection.public_url}[/dark_orange][/bold]\n\n")

        atexit.register(self.close)

    def run(self):
        print("""[dark_orange]
                    NOTE :
                        uses port 8088
                        installs tor if not found
                        runs tor service#

                   Example :
                        ngrok_url:port/<****.onion> or http://localhost:8088/<darkwebspagejknewlkn11232.onion>
                 #

                        [/dark_orange]""")

        uvicorn.run(
            app,
            host="localhost",
            port=8088,
        )