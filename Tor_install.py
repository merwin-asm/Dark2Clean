import subprocess
import requests
import platform
import os

from bs4 import BeautifulSoup


def check_tor_installed():
    try:
        subprocess.check_output(['tor', '--version'])
        return True
    except OSError:
        return False

def install_tor_windows():
    # Download Tor browser bundle for Windows
    download_url = get_latest_version_link()
    response = requests.get(download_url)
    tor_installer_path = "torbrowser-install.exe"
    
    # Save the Tor installer
    with open(tor_installer_path, 'wb') as f:
        f.write(response.content)
    
    # Run the Tor installer silently
    subprocess.run([tor_installer_path, '/S'])

    # Clean up the installer
    os.remove(tor_installer_path)

def install_tor_linux():
    # Install Tor using the package manager
    subprocess.run(['sudo', 'apt', 'install', '-y', 'tor'])

def install_tor_macos():
    # Install Tor using Homebrew package manager
    subprocess.run(['brew', 'install', 'tor'])

def install_tor():
    if platform.system() == 'Windows':
        install_tor_windows()
    elif platform.system() == 'Linux':
        install_tor_linux()
    elif platform.system() == 'Darwin':
        install_tor_macos()

def get_latest_version_link():
    url = 'https://www.torproject.org/download/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    link = soup.find('a', attrs={'class': 'downloadLink'}, string="Download for Windows")

    if link is not None:
        href = link.get('href')
        return create_download_link(href)
    else:
        print('Cant get a valid windows download link from https://www.torproject.org/download/')
        exit()

def create_download_link(href):
    return 'https://www.torproject.org' + href
        


