from datetime import datetime

from app.models.Breed import Breed
from app.models.Bull import Bull
from app.models.Cow import Cow
from app.models.EarTag import EarTag
from app.models.Herd import Herd


def main():
    print("Iniciando o sistema de gerenciamento de bovinos...")

    # Criando o rebanho
    herd = Herd()

    # Criando brincos de identificação (EarTags) e atribuindo a bovinos
    eartag_bull1 = EarTag(1, "red")
    eartag_bull2 = EarTag(2, "red")
    eartag_cow1 = EarTag(3, "yellow")
    eartag_cow2 = EarTag(4, "yellow")

    # Criando touros e vacas com os brincos de identificação
    print("\n--- Criando touros ---")
    bull1 = Bull(eartag_bull1, datetime(2019, 5, 21), 314.3, Breed.ANGUS)
    bull2 = Bull(eartag_bull2, datetime(2020, 6, 30), 320.6, Breed.HOLSTEIN)
    print(f"Touro criado: {bull1.__str__()}")
    print(f"Touro criado: {bull2.__str__()}")

    print("\n--- Criando vacas ---")
    cow1 = Cow(eartag_cow1, datetime(2021, 3, 15), 320.5, Breed.JERSEY)
    cow2 = Cow(eartag_cow2, datetime(2022, 1, 10), 340.1, Breed.JERSEY)
    print(f"Vaca criada: {cow1.__str__()}")
    print(f"Vaca criada: {cow2.__str__()}")

    # Adicionando bovinos ao rebanho
    print("\n--- Adicionando bovinos ao rebanho ---")
    herd.add_cattle(bull1)
    herd.add_cattle(bull2)
    herd.add_cattle(cow1)
    herd.add_cattle(cow2)
    print(f"Bovinos no rebanho: {herd.__str__()}")

    # Adicionando histórico de produção de leite às vacas
    print("\n--- Adicionando histórico de produção de leite para vacas ---")
    cow1.add_milk_production(datetime(2024, 10, 1), 20, 8.5, 3.5, 4.1)
    cow2.add_milk_production(datetime(2024, 10, 15), 22, 9.0, 3.7, 4.3)
    print(f"Histórico de produção das vacas: {cow1.__str__()} \n{cow2.__str__()}")


if __name__ == "__main__":
    main()
