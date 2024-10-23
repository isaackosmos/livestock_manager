class EarTag:
    def __init__(self, number: int, color: str) -> None:
        self.__number = number
        self.__color = color

    @property
    def number(self) -> int:
        return self.__number

    @property
    def color(self) -> str:
        return self.__color

    def __str__(self) -> str:
        return f"EarTag: {self.__number}, {self.__color}"