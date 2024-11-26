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

    # Criando brincos de identificação e atribuindo aos bovinos
    ear_tag_bull1 = EarTag(1, "red")
    ear_tag_cow1 = EarTag(3, "yellow")

    # Criando touro e vaca com os brincos de identificação
    bull1 = Bull(ear_tag_bull1, datetime(2019, 5, 21), 314.3, Breed.ANGUS)
    cow1 = Cow(ear_tag_cow1, datetime(2021, 3, 15), 320.5, Breed.JERSEY)

    # Adicionando bovinos ao rebanho
    herd.add_cattle(bull1)
    herd.add_cattle(cow1)

    # Lendo um bovino
    print("\n--- Lendo um bovino ---")
    bovine = herd.get_cattle(1)
    if bovine:
        print(f"Bovino encontrado: {bovine}")

    # Atualizando um bovino
    print("\n--- Atualizando um bovino ---")
    new_bull1 = Bull(ear_tag_bull1, datetime(2019, 5, 21), 320.0, Breed.ANGUS)
    try:
        herd.update_cattle(1, new_bull1)
        print("Bovino atualizado com sucesso.")
    except ValueError as e:
        print(f"Erro ao atualizar bovino: {e}")

    # Deletando um bovino
    print("\n--- Deletando um bovino ---")
    try:
        herd.delete_cattle(1)
        print("Bovino deletado com sucesso.")
    except ValueError as e:
        print(f"Erro ao deletar bovino: {e}")

    # Adicionando produção de leite a uma vaca
    print("\n--- Adicionando produção de leite ---")
    cow1.add_milk_production(datetime(2023, 10, 1), 20.5, 8.5, 3.5, 1.2)
    cow1.add_milk_production(datetime(2023, 10, 2), 22.0, 8.7, 3.6, 1.3)

    # Lendo produção de leite
    print("\n--- Lendo produção de leite ---")
    try:
        milk_production = cow1.get_milk_production(datetime(2023, 10, 1))
        print(f"Produção de leite encontrada: {milk_production}")
    except ValueError as e:
        print(f"Erro ao ler produção de leite: {e}")

    # Atualizando produção de leite
    print("\n--- Atualizando produção de leite ---")
    try:
        cow1.update_milk_production(datetime(2023, 10, 1), 21.0, 8.6, 3.5, 1.2)
        print("Produção de leite atualizada com sucesso.")
    except ValueError as e:
        print(f"Erro ao atualizar produção de leite: {e}")

    # Deletando produção de leite
    print("\n--- Deletando produção de leite ---")
    try:
        cow1.delete_milk_production(datetime(2023, 10, 1))
        print("Produção de leite deletada com sucesso.")
    except ValueError as e:
        print(f"Erro ao deletar produção de leite: {e}")

    print(f"Bovinos no rebanho: {herd}")

if __name__ == "__main__":
    main()
