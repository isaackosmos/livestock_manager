from datetime import datetime

from app.models.MilkQualityControl import MilkQualityControl


class MilkProduction:
    def __init__(self, date: datetime, liters: float, milk_quality_control: MilkQualityControl) -> None:
        if not isinstance(milk_quality_control, MilkQualityControl):
            raise ValueError("milk_quality_control must be an instance of MilkQualityControl")
        self.date = date
        self.liters = liters
        self.__milk_quality_control = milk_quality_control

    @property
    def date(self) -> datetime:
        return self.__date

    @property
    def liters(self) -> float:
        return self.__liters

    @property
    def milk_quality_control(self) -> MilkQualityControl:
        return self.__milk_quality_control

    @date.setter
    def date(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise ValueError("date must be an instance of datetime")
        if value > datetime.now():
            raise ValueError("date cannot be in the future")
        self.__date = value

    @liters.setter
    def liters(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise ValueError("liters must be a number")
        if value < 0:
            raise ValueError("liters cannot be negative")
        self.__liters = value

    def get_milk_quality_control(self) -> MilkQualityControl:
        return self.__milk_quality_control

    def update_milk_quality_control(self, score: float, fat_percentage: float, vitamins_percentage: float) -> None:
        self.__milk_quality_control = MilkQualityControl(score, fat_percentage, vitamins_percentage)

    def delete_milk_quality_control(self) -> None:
        self.__milk_quality_control = None

    def __str__(self) -> str:
        return f"MilkProduction: {self.__date}, {self.__liters}, {self.__milk_quality_control.__str__()}"
