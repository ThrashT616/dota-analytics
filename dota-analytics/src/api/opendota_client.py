import requests
from src.services.hero_service import transform_heroes
from src.repositores.hero_repository import insert_heroes
from src.services.item_service import transform_items
from src.repositores.item_repository import insert_items
from src.database.connection import get_connection

BASE_URL = "https://api.opendota.com/api"

def get_heroes():
    response = requests.get(f"{BASE_URL}/heroes")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    heroes_api = get_heroes()
    heroes = transform_heroes(heroes_api)

    insert_heroes(heroes)

    print(f"{len(heroes)} heróis processados com sucesso!")

def get_items():
    response = requests.get(f"{BASE_URL}/constants/items")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":

    items_api = get_items()
    items = transform_items(items_api)
    insert_items(items)

    print(f"{len(items)} itens processado com sucesso!")


def get_match():
    response = requests.get(f"{BASE_URL}/matches/{8377028174}")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":

    match = get_match()
    print(match.keys())