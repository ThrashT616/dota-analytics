def normalize_numeric(value):
    if value is False or value is True:
        return None
    return value


def normalize_boolean(value):
    if isinstance(value, bool):
        return None
    return value



def transform_item(item_name: str, item_api: dict) -> dict:
    return{
        "id": item_api["id"],
        "name": item_name,
        "dname": item_api.get("dname"),
        "qual": item_api.get("qual"),
        "cost": item_api.get("cost"),
        "behavior": item_api.get("behavior"),
        "mc": normalize_boolean(item_api.get("mc")),
        "hc": normalize_boolean(item_api.get("hc")),
        "cd": normalize_numeric(item_api.get("cd")),
        "created": normalize_boolean(item_api.get("created")),
    }


def transform_items(items_api: dict) -> list[dict]:
    return[
        transform_item(item_name, item_data)
        for item_name, item_data in items_api.items()
    ]