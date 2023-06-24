import os
import subprocess

import requests
from bs4 import BeautifulSoup

from .os_interaction import OSInteraction


class WindowsInteraction(OSInteraction):
    def start(self) -> None:
        subprocess.run(['net', 'start', 'tor'])

    def install(self) -> None:
        # Download Tor browser bundle for Windows
        download_url = self.__get_latest_version_link()
        response = requests.get(download_url)
        tor_installer_path = "torbrowser-install.exe"

        # Save the Tor installer
        with open(tor_installer_path, 'wb') as file:
            file.write(response.content)

        # Run the Tor installer silently
        subprocess.run([tor_installer_path, '/S'])

        # Clean up the installer
        os.remove(tor_installer_path)

    def __get_latest_version_link(self):
        url = 'https://www.torproject.org/download/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        link = soup.find('a', attrs={'class': 'downloadLink'}, string="Download for Windows")

        if link is not None:
            href = link.get('href')
            return self.__create_download_link(href)
        else:
            print('Cant get a windows download link from https://www.torproject.org/download/')
            exit()

    def __create_download_link(self, href):
        return 'https://www.torproject.org' + href
