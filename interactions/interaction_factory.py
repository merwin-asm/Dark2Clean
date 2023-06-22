from interactions.os import WindowsInteraction, LinuxInteraction, MacosInteraction, OSInteraction


class InteractionFactory:
    @staticmethod
    def get_interaction(operative_system: str) -> OSInteraction:
        if 'darwin' in operative_system:
            return MacosInteraction()
        elif 'linux' in operative_system:
            return LinuxInteraction()
        elif 'win' in operative_system:
            return WindowsInteraction()
        else:
            print('Unsupported operative system')
            exit()
