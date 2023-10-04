import sqlite3
import w1thermsensor
from database import Database

def setup():
    with Database(connection) as database:
        database.cursor.execute('''
                                CREATE TABLE temperatures
                                (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    temperature REAL NOT NULL,
                                    measurement_time DATE NOT NULL
                                )
                    ''')


sensor = w1thermsensor.W1ThermSensor()

print(sensor.get_temperature())


connection = sqlite3.connect('database.db')

