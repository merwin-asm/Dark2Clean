import subprocess

from .os_interaction import OSInteraction


class LinuxInteraction(OSInteraction):
    def install(self) -> None:
        # Install Tor using the package manager
        subprocess.run(['sudo', 'apt', 'install', '-y', 'tor'])