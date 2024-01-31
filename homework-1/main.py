"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from north_data import config


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
        cur.copy_from(f, NAME_DB[index], sep=',')
        conn.commit()

    conn.close()


if __name__ == '__main__':
    for index in range(len(config.NAME_BD)):
        try:
            load_db(index, config.DATA, config.NAME_BD)
        except psycopg2.errors.BadCopyFileFormat:
            continue
