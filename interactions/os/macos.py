import subprocess

from .os_interaction import OSInteraction


class MacosInteraction(OSInteraction):
    def install(self) -> None:
        # Install Tor using Homebrew package manager
        subprocess.run(['brew', 'install', 'tor'])
