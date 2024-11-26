from abc import ABC, abstractmethod
from datetime import datetime

from app.models.Breed import Breed
from app.models.EarTag import EarTag


class Bovine(ABC):
    def __init__(self, ear_tag: EarTag, birth: datetime, weight: float, breed: Breed) -> None:
        if not isinstance(ear_tag, EarTag):
            raise ValueError("ear_tag must be an instance of EarTag")
        if not isinstance(birth, datetime):
            raise ValueError("birth must be an instance of datetime")
        if not isinstance(weight, (float, int)):
            raise ValueError("weight must be a number")
        if not isinstance(breed, Breed):
            raise ValueError("breed must be an instance of Breed")
        self.__ear_tag = ear_tag
        self.__birth = birth
        self.__weight = weight
        self.__breed = breed

    @property
    def ear_tag(self) -> EarTag:
        return self.__ear_tag

    @property
    def age(self) -> int:
        today = datetime.today().date()
        years = today.year - self.__birth.year
        months = today.month - self.__birth.month
        return years*12 + months

    @property
    def breed(self) -> Breed:
        return self.__breed

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        if not isinstance(weight, (float, int)):
            raise ValueError("weight must be a number")
        self.__weight = weight

    @abstractmethod
    def __str__(self) -> str:
        pass
