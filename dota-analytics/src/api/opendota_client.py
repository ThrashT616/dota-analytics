import requests
from src.services.hero_service import transform_heroes
from src.repositores.hero_repository import insert_heroes
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

    for key, item in list(items_api.items())[:20]:
        print(key)
        print(item)
        print("-" * 50)