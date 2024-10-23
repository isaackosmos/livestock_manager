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

    def __str__(self) -> str:
        string = "Herd:\n"

        for cattle in self.__cattle:
            string += f"{cattle['bovine'].__str__()}, added on {cattle['date_added']}\n"

        return string