from app.models.Bovine import Bovine


class Bull(Bovine):
    def __str__(self) -> str:
        return f"Bull: {self.ear_tag.__str__()}, {self.weight} kg, {self.age} months, {self.breed}"
