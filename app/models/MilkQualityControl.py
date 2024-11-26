class MilkQualityControl:
    def __init__(self, score: float, fat_percentage: float, vitamins_percentage: float) -> None:
        self.score = score
        self.fat_percentage = fat_percentage
        self.vitamins_percentage = vitamins_percentage

    @property
    def score(self) -> float:
        return self.__score

    @property
    def fat_percentage(self) -> float:
        return self.__fat_percentage

    @property
    def vitamins_percentage(self) -> float:
        return self.__vitamins_percentage

    @score.setter
    def score(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise ValueError("score must be a number")
        if value < 0:
            raise ValueError("score cannot be negative")
        self.__score = value

    @fat_percentage.setter
    def fat_percentage(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise ValueError("fat_percentage must be a number")
        if value < 0:
            raise ValueError("fat_percentage cannot be negative")
        self.__fat_percentage = value

    @vitamins_percentage.setter
    def vitamins_percentage(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise ValueError("vitamins_percentage must be a number")
        if value < 0:
            raise ValueError("vitamins_percentage cannot be negative")
        self.__vitamins_percentage = value

    def __str__(self):
        return f"MilkQualityControl: {self.__score}, {self.__fat_percentage}, {self.__vitamins_percentage}"