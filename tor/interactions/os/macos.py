import subprocess

from .os_interaction import OSInteraction


class MacosInteraction(OSInteraction):
    def start(self) -> None:
        subprocess.run(['sudo', 'launchctl', 'start', 'homebrew.mxcl.tor'])

    def install(self) -> None:
        # Install Tor using Homebrew package manager
        subprocess.run(['brew', 'install', 'tor'])
