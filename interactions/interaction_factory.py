from interactions.os import WindowsInteraction, LinuxInteraction, MacosInteraction, OSInteraction


class InteractionFactory:
    @staticmethod
    def get_interaction(operative_system: str) -> OSInteraction:
        if 'win' in operative_system:
            return WindowsInteraction()
        elif 'linux' in operative_system:
            return LinuxInteraction()
        elif 'darwin' in operative_system:
            return MacosInteraction()
        else:
            print('Unsupported operative system')
            exit()
