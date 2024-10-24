class MilkQualityControl:
    def __init__(self, score: float, fat_percentage: float, vitamins_percentage: float) -> None:
        if not isinstance(score, (float, int)):
            raise ValueError("score must be a number")

        if not isinstance(fat_percentage, (float, int)):
            raise ValueError("fat_percentage must be a number")

        if not isinstance(vitamins_percentage, (float, int)):
            raise ValueError("vitamins_percentage must be a number")

        self.__score = score
        self.__fat_percentage = fat_percentage
        self.__vitamins_percentage = vitamins_percentage

    @property
    def score(self) -> float:
        return self.__score

    @property
    def fat_percentage(self) -> float:
        return self.__fat_percentage

    @property
    def vitamins_percentage(self) -> float:
        return self.__vitamins_percentage

    def __str__(self):
        return f"MilkQualityControl: {self.__score}, {self.__fat_percentage}, {self.__vitamins_percentage}"