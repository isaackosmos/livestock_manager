from datetime import datetime
from xmlrpc.client import DateTime

from app.models.Bovine import Bovine
from app.models.Breed import Breed
from app.models.EarTag import EarTag
from app.models.MilkProduction import MilkProduction
from app.models.MilkQualityControl import MilkQualityControl


class Cow(Bovine):
    def __init__(self, ear_tag: EarTag, birth: datetime, weight: float, breed: Breed) -> None:
        super().__init__(ear_tag, birth, weight, breed)
        self.__milk_production_history = []

    @property
    def milk_production_history(self) -> list:
        return self.__milk_production_history

    def add_milk_production(self, date: datetime, liters: float, score: float, fat_percentage: float,
                            vitamins_percentage: float) -> None:
        milk_quality_control = MilkQualityControl(score, fat_percentage, vitamins_percentage)
        milk_production = MilkProduction(date, liters, milk_quality_control)
        self.__milk_production_history.append(milk_production)

    def get_milk_production(self, date: datetime) -> MilkProduction|None:
        if not isinstance(date, datetime):
            raise ValueError("date must be an instance of datetime")
        for milk in self.__milk_production_history:
            if milk.date == date:
                return milk
        raise ValueError(f"Milk production on {date} not found")

    def update_milk_production(self, date: datetime, liters: float, score: float, fat_percentage: float,
                               vitamins_percentage: float) -> None:
        if not isinstance(date, datetime):
            raise ValueError("date must be an instance of datetime")
        if not isinstance(liters, (float, int)):
            raise ValueError("liters must be a number")
        if not isinstance(score, (float, int)):
            raise ValueError("score must be a number")
        if not isinstance(fat_percentage, (float, int)):
            raise ValueError("fat_percentage must be a number")
        if not isinstance(vitamins_percentage, (float, int)):
            raise ValueError("vitamins_percentage must be a number")
        for milk in self.__milk_production_history:
            if milk.date == date:
                milk.liters = liters
                milk.milk_quality_control.score = score
                milk.milk_quality_control.fat_percentage = fat_percentage
                milk.milk_quality_control.vitamins_percentage = vitamins_percentage
                return
        raise ValueError(f"Milk production on {date} not found")

    def delete_milk_production(self, date: datetime) -> None:
        if not isinstance(date, datetime):
            raise ValueError("date must be an instance of datetime")
        for milk in self.__milk_production_history:
            if milk.date == date:
                self.__milk_production_history.remove(milk)
                return
        raise ValueError(f"Milk production on {date} not found")

    def __str__(self) -> str:
        string = (f"Cow: {self.ear_tag.__str__()}, {self.weight} kg, {self.age} months, "
                  f"{self.breed}, milk production history: \n")
        for milk in self.milk_production_history:
            string += milk.__str__() + "\n"
        return string
