from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException
import requests
import uvicorn

from tor import Tor
from converters import OptionToProtocolConverter
from pyngrok import ngrok
from rich import print
import atexit


_connection = None
app = FastAPI()


@app.get('/{e}', response_class=HTMLResponse)
async def get(onion_url):
    tor_proxy = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    if not onion_url.startswith("http://") or onion_url.startswith("https://"):
        onion_url = "http://" + onion_url

    try:
        response = requests.get(onion_url, proxies=tor_proxy)
        return response.text
    except:
        raise HTTPException(status_code=500, detail="Server error")


def close():
    global _connection

    ngrok.disconnect(_connection.public_url)


def start_ngrok(auth, protocol_option):
    global _connection

    ngrok.set_auth_token(auth)
    protocol = OptionToProtocolConverter.convert(protocol_option)
    _connection = ngrok.connect(8088, protocol)
    print(f"\n[bold][dark_orange]Ngrok Public URL : {_connection.public_url}[/dark_orange][/bold]\n\n")

    atexit.register(close)


def set_privacy():
    if input("Public or Private (1/2): ") == "1":
        start_ngrok(input("Ngrok Auth : "), input("1 Http or 2 Https (note using https can get 'your ip expossed') : "))
    else:
        print(f"\n[bold][dark_orange]Private URL : http://localhost:8088[/dark_orange][/bold]\n\n")


def run_server():
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


def main():
    tor: Tor = Tor()

    tor.install()
    tor.start()
    set_privacy()
    run_server()


if __name__ == '__main__':
    main()
