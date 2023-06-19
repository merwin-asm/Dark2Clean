import subprocess
import sys

from interactions import InteractionFactory
from interactions.os import OSInteraction


def check_tor_installed():
    try:
        subprocess.check_output(['tor', '--version'])
        return True
    except OSError:
        return False


def install_tor():
    interaction: OSInteraction = InteractionFactory.get_interaction(sys.platform)
    interaction.install()


