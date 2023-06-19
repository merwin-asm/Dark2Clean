from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException
import requests
import uvicorn

from Tor_install import *
from pyngrok import ngrok
from rich import print
import atexit


_connection = None
tor_proxy = {
     'http': 'socks5h://localhost:9050',
     'https': 'socks5h://localhost:9050'
}
app = FastAPI()


@app.get('/{e}', response_class=HTMLResponse)
async def get(e):
    if not e.startswith("http://") or e.startswith("https://"):
        e = "http://" + e

    try:
        t = requests.get(e, proxies=tor_proxy)
        return t.text
    except:
        raise HTTPException(status_code=500, detail="Server error")


def start_tor():
    print("[green]  [+] Starting Tor [/green]")

    interaction = InteractionFactory.get_interaction(sys.platform)
    interaction.start()

    print("[green]  [+] Tor service restarted successfully.[/green]")


def close():
    global _connection

    ngrok.disconnect(_connection.public_url)


def start_ngrok(auth, t):
    global _connection

    ngrok.set_auth_token(auth)
    
    if t == "2":
        _connection = ngrok.connect(8088, "http")
    else:
        _connection = ngrok.connect(8088, "tcp")

    print(f"\n[bold][dark_orange]Ngrok Public URL : {_connection.public_url}[/dark_orange][/bold]\n\n")

    atexit.register(close)


def try_to_install_tor():
    print("[blue]  [=] Checking if Tor installed[/blue]")
    if not check_tor_installed():
        print("[red]  [-] Tor not found -- >  Installing Tor[/red]")
        try:
            install_tor()
            print("[green]  [+] Installed Tor[/green]")
        except:
            print("[red]  [-] Tor couldn't be installed -- > Exiting[/red]")
            exit()


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
    try_to_install_tor()
    start_tor()
    set_privacy()
    run_server()


if __name__ == '__main__':
    main()
