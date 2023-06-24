from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException
import requests

from ngrok.ngrok import Ngrok
from tor import Tor


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


def main():
    tor: Tor = Tor()
    ngrok: Ngrok = Ngrok()

    tor.install()
    tor.start()
    ngrok.set_privacy()
    ngrok.run()


if __name__ == '__main__':
    main()
