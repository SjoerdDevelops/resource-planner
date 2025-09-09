from peewee import SqliteDatabase
from infrastructure.models import EmployeeModel
from enum import Enum


class Environment(str, Enum):
    DEV = ":memory:"
    TEST = ":memory:"
    PROD = "database.db"


def create_db(environment: Environment) -> SqliteDatabase:
    return SqliteDatabase(environment)


def init_db() -> None:
    db = create_db(Environment.DEV)
    db.bind([EmployeeModel])
    _ = db.connect()
    db.create_tables([EmployeeModel])
