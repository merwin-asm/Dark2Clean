import subprocess
import requests
import platform
import os




def check_tor_installed():
    try:
        subprocess.check_output(['tor', '--version'])
        return True
    except OSError:
        return False

def install_tor_windows():
    # Download Tor browser bundle for Windows
    download_url = "https://www.torproject.org/dist/torbrowser/10.5.2/torbrowser-install-10.5.2_en-US.exe"
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
        


