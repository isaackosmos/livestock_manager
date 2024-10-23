from datetime import datetime

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

    def __str__(self) -> str:
        string = (f"Cow: {self.ear_tag.__str__()}, {self.weight} kg, {self.age} months, "
                  f"{self.breed}, milk production history: \n")

        for milk in self.milk_production_history:
            string += milk.__str__() + "\n"

        return string
