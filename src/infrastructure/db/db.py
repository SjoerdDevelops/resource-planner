from peewee import SqliteDatabase
from infrastructure.models import EmployeeModel

db = SqliteDatabase("database.db")


def init_db():
    db.bind([EmployeeModel])
    db.connect()
    db.create_tables([EmployeeModel])
