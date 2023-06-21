import os
import subprocess

import requests

from .os_interaction import OSInteraction


class WindowsInteraction(OSInteraction):
    def start(self) -> None:
        subprocess.run(['net', 'start', 'tor'])

    def install(self) -> None:
        # Download Tor browser bundle for Windows
        # TODO: something to get always the latest version
        download_url = "https://dist.torproject.org/torbrowser/12.0.7/torbrowser-install-win64-12.0.7_ALL.exe"
        response = requests.get(download_url)
        tor_installer_path = "torbrowser-install.exe"

        # Save the Tor installer
        with open(tor_installer_path, 'wb') as file:
            file.write(response.content)

        # Run the Tor installer silently
        subprocess.run([tor_installer_path, '/S'])

        # Clean up the installer
        os.remove(tor_installer_path)
