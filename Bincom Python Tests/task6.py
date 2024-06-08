# QUE6: Save the colours and their frequencies in postgresql database

import psycopg2
from data import get_color_frequencies


def save_to_postgress():
    connect = psycopg2.connect(
        dbname="Bincom_database",
        username="Olalekan",
        password="Bincom2024",
        host="localhost"
    )

    cur = connect.cursor()

    # creating database table
    cur.execute(""""
    CREATE TABLE IF NOT EXISTS color_frequencies (
    color VARCHAR(20) PRIMARY KEY,
    frequency INTEGER
    )
    """)

    # Inserting data
    color_freq = get_color_frequencies()
    for color, freq in color_freq.items():
        cur.execute(
            "INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s) "
            "ON CONFLICT (color) DO UPDATE SET frequency = %s", (color, freq, freq))

    connect.commit()
    cur.close()
    connect.close()
    print("colors and frequencies successfully saved to postgress")


save_to_postgress()


