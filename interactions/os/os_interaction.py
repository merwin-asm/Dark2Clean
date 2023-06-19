from abc import abstractmethod, ABCMeta


class OSInteraction(metaclass=ABCMeta):
    @abstractmethod
    def install(self) -> None:
        pass

    @abstractmethod
    def start(self) -> None:
        pass
