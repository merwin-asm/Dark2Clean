from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException
from rich import print
import uvicorn
import requests
import time
import sys

from Tor_install import *
from pyngrok import ngrok
from rich import print
import atexit


_connection = None


print("[blue]  [=] Checking if Tor installed[/blue]")
if not check_tor_installed():
    print("[red]  [-] Tor not found -- >  Installing Tor[/red]")
    try:
        install_tor()
        print("[green]  [+] Installed Tor[/green]")
    except:
        print("[red]  [-] Tor couldn't be installed -- > Exiting[/red]")
        exit()


print("[green]  [+] Starting Tor [/green]")



def start_tor():


    if sys.platform.startswith('linux'):
        subprocess.run(['sudo', 'service', 'tor', 'start'])
    elif sys.platform.startswith('win'):
        subprocess.run(['net', 'start', 'tor'])
    elif sys.platform.startswith('darwin'):
        subprocess.run(['sudo', 'launchctl', 'start', 'homebrew.mxcl.tor'])
    else:
        print("[red]  [-] Unsupported operating system. [/red]")
        exit()

    print("[green]  [+] Tor service restarted successfully.[/green]")


start_tor()

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

if input("Public or Private (1/2): ") == "1":
    start_ngrok(input("Ngrok Auth : "), input("1 Http or 2 Https (note using https can get 'your ip expossed') : "))
else:
    print(f"\n[bold][dark_orange]Private URL : http://localhost:8088[/dark_orange][/bold]\n\n")

print("""[dark_orange]
        NOTE : 
            uses port 8088
            installs tor if not found
            runs tor service

        Example :
            ngrok_url:port/<****.onion> or http://localhost:8088/<darkwebspagejknewlkn11232.onion>
     

            [/dark_orange]""")



uvicorn.run(
            app,
            host= "localhost",
            port= 8088,
)


