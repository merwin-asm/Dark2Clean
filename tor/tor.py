import subprocess
import sys

from .interactions import InteractionFactory
from .interactions.os import OSInteraction


class Tor:
    def __init__(self):
        self.interaction: OSInteraction = InteractionFactory.get_interaction(sys.platform)

    def is_installed(self) -> bool:
        try:
            subprocess.check_output(['tor', '--version'])
            return True
        except OSError:
            return False

    def install(self) -> None:
        print("[blue]  [=] Checking if Tor installed[/blue]")
        if not self.is_installed():
            print("[red]  [-] Tor not found -- >  Installing Tor[/red]")
            try:
                self.interaction.install()
            except:
                print("[red]  [-] Tor couldn't be installed -- > Exiting[/red]")
                exit()

    def start(self) -> None:
        print("[green]  [+] Starting Tor [/green]")
        self.interaction.start()
        print("[green]  [+] Tor service restarted successfully.[/green]")
