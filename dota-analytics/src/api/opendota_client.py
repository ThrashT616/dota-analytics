import requests
from src.services.hero_service import transform_heroes

BASE_URL = "https://api.opendota.com/api"

def get_heroes():
    response = requests.get(f"{BASE_URL}/heroes")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":

    heroes_api = get_heroes()

    heroes = transform_heroes(heroes_api)

    for hero in heroes[:10]:
        print(hero)

    
