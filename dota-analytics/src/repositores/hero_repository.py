from src.database.connection import get_connection

def insert_hero(hero):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:

            cursor.execute("""
                 INSERT INTO hero (   
                    id,
                    name,
                    localized_name,
                    primary_attr,
                    attack_type,
                    roles,
                    legs       
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING
            """, (
                 hero["id"],      
                 hero["name"],   
                 hero["localized_name"],   
                 hero["primary_attr"],   
                 hero["attack_type"],   
                 hero["roles"],   
                 hero["legs"],   
            ))


        conn.commit()


    finally:
        conn.close()