from abc import ABC, abstractmethod
from datetime import datetime

from app.models.Breed import Breed
from app.models.EarTag import EarTag


class Bovine(ABC):
    def __init__(self, ear_tag: EarTag, birth: datetime, weight: float, breed: Breed) -> None:
        self.ear_tag = ear_tag
        self.birth = birth
        self.weight = weight
        self.breed = breed

    @property
    def ear_tag(self) -> EarTag:
        return self.__ear_tag

    @property
    def birth(self) -> datetime:
        return self.__birth

    @property
    def age(self) -> int:
        today = datetime.today().date()
        years = today.year - self.__birth.year
        months = today.month - self.__birth.month
        return years * 12 + months

    @property
    def weight(self) -> float:
        return self.__weight

    @property
    def breed(self) -> Breed:
        return self.__breed

    @ear_tag.setter
    def ear_tag(self, ear_tag: EarTag) -> None:
        if not isinstance(ear_tag, EarTag):
            raise ValueError("ear_tag must be an instance of EarTag")
        self.__ear_tag = ear_tag

    @birth.setter
    def birth(self, birth: datetime) -> None:
        if not isinstance(birth, datetime):
            raise ValueError("birth must be an instance of datetime")
        if birth > datetime.now():
            raise ValueError("birth cannot be in the future")
        self.__birth = birth

    @weight.setter
    def weight(self, weight: float) -> None:
        if not isinstance(weight, (float, int)):
            raise ValueError("weight must be a number")
        if weight < 0:
            raise ValueError("weight cannot be negative")
        self.__weight = weight

    @breed.setter
    def breed(self, breed: Breed) -> None:
        if not isinstance(breed, Breed):
            raise ValueError("breed must be an instance of Breed")
        self.__breed = breed

    @abstractmethod
    def __str__(self) -> str:
        pass
