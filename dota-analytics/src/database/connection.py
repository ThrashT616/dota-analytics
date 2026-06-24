import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="dota_analytics",
        user="postgres",
        password="postgres"
    )