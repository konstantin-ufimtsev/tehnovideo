import psycopg2
from config import *


def write_to_database(data: dict):
    """
    'id' serial PRIMARY KEY
    "date" - DATE
    'url' -  VARCHAR
    'sku_name' - VARCHAR
    'article' - VARCHAR
    "current_price' - NUMERIC
    'type' - VARCHAR
    'model' - VARCHAR
    """
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        connection.autocommit = True
        
        date = data['date']
        url = data['url']
        sku_name = data['sku_name']
        article = data['article']
        current_price = data['current_price']
        type = data['type']
        model = data['model']
        
        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tehnovideo (date, url, sku_name, article, current_price, type, model) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (date, url, sku_name, article, current_price, type, model)
            )
    
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL,', _ex)