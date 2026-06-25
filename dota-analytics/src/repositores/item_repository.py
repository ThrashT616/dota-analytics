from src.database.connection import get_connection


def insert_items(items: list[dict]) -> None:
    conn = get_connection ()

    try:
        with conn.cursor() as cursor:
            for item in items:
                cursor.execute("""
                    INSERT INTO item (
                        id,         
                        name,
                        dname,
                        qual,       
                        cost,
                        behavior,
                        mc,
                        hc,
                        cd,
                        created
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (id) DO NOTHING
                    """, (
                         item["id"],
                         item["name"],
                         item["dname"],
                         item["qual"],
                         item["cost"],
                         item["behavior"],
                         item["mc"],
                         item["hc"],
                         item["cd"],
                         item["created"]
                    ))
                
        conn.commit()

    finally:
        conn.close()            