import subprocess

from .os_interaction import OSInteraction


class LinuxInteraction(OSInteraction):
    def start(self) -> None:
        subprocess.run(['sudo', 'service', 'tor', 'start'])

    def install(self) -> None:
        # Install Tor using the package manager
        subprocess.run(['sudo', 'apt', 'install', '-y', 'tor'])
