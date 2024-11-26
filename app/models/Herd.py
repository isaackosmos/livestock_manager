from typing import List, Dict
from datetime import datetime

from app.models.Bovine import Bovine


class Herd:
    def __init__(self):
        self.__cattle = []

    @property
    def cattle(self) -> List[Dict]:
        return self.__cattle

    def add_cattle(self, bovine: Bovine) -> None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__cattle.append({
            "bovine": bovine,
            "date_added": now
        })

    def get_cattle(self, ear_tag_number: int) -> Bovine:
        for cattle in self.__cattle:
            if cattle["bovine"].ear_tag.number == ear_tag_number:
                return cattle["bovine"]
        raise ValueError(f"Cattle with ear tag number {ear_tag_number} not found")

    def update_cattle(self, ear_tag_number: int, bovine: Bovine) -> None:
        if not isinstance(ear_tag_number, int):
            raise ValueError("ear_tag_number must be a number")
        if not isinstance(bovine, Bovine):
            raise ValueError("bovine must be an instance of Bovine")
        for cattle in self.__cattle:
            if cattle["bovine"].ear_tag.number == ear_tag_number:
                cattle["bovine"] = bovine
                return
        raise ValueError(f"Cattle with ear tag number {ear_tag_number} not found")

    def delete_cattle(self, ear_tag_number: int) -> None:
        for cattle in self.__cattle:
            if cattle["bovine"].ear_tag.number == ear_tag_number:
                self.__cattle.remove(cattle)
                return
        raise ValueError(f"Cattle with ear tag number {ear_tag_number} not found")

    def __str__(self) -> str:
        string = "Herd:\n"
        for cattle in self.__cattle:
            string += f"{cattle['bovine'].__str__()}, added on {cattle['date_added']}\n"
        return string
