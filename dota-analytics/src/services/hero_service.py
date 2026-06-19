def transform_hero(hero_api: dict) -> dict:
    return {
        "id": hero_api["id"],
        "name": hero_api["name"],
        "localized_name": hero_api ["localized_name"],
        "primary_attr": hero_api ["primary_attr"],
        "attack_type": hero_api ["attack_type"],
        "roles": hero_api ["roles"],
        "legs": hero_api ["legs"],
    }

def transform_heroes(heroes_api: list[dict]) -> list[dict]:
    return[transform_hero(hero) for hero in heroes_api]