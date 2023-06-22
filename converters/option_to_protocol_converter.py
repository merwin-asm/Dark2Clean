class OptionToProtocolConverter:
    @staticmethod
    def convert(option: str):
        if option == "2":
            return "http"
        else:
            return "https"
