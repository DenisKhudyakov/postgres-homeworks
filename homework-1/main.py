"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from north_data import config
import pandas as pd
from sqlalchemy import create_engine

def load_db(index: int, DATA: tuple, NAME_DB: tuple) -> None:
    """Функция, которая загружает .csv таблицы в psql"""
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="279211"
    )

    cur = conn.cursor()

    with open(DATA[index], 'r') as f:
        next(f)
        cur.copy_from(f, NAME_DB[index], sep=",")
        conn.commit()

    conn.close()


if __name__ == '__main__':
    # for index in range(len(config.NAME_BD)):
    #     load_db(index, config.DATA, config.NAME_BD)
    engine = create_engine('postgresql://postgres:279211@localhost:5432/north')
    df1 = pd.read_csv(config.EMPLOYEES)
    df2 = pd.read_csv(config.ORDERS)
    df3 = pd.read_csv(config.CUSTOMER)
    df1.to_sql('employees_data', engine)
    df2.to_sql('orders_data', engine)
    df3.to_sql('customers_data', engine)


