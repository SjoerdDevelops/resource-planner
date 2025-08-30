from dataclasses import dataclass
from typing import List, Optional
from peewee import SqliteDatabase, Model, CharField, DoubleField, IntegerField


@dataclass
class Employee:
    id: Optional[int]
    name: str
    fte: float
    utilization_rate: float


db = SqliteDatabase("database.db")


class EmployeeModel(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    fte = DoubleField()
    utilization_rate = DoubleField()

    class Meta:
        database = db


def create_employee(name: str, fte: float, utilization_rate: float) -> Employee:
    return Employee(None, name, fte, utilization_rate)


class Persistance:
    def __init__(self):
        db.connect()
        db.create_tables([EmployeeModel])

    def __del__(self):
        db.close()

    def store_employee(self, employee: Employee) -> None:
        EmployeeModel.create(
            name=employee.name,
            fte=employee.fte,
            utilization_rate=employee.utilization_rate,
        )

    def fetch_employees(self) -> List[Employee]:
        employees = EmployeeModel.select()
        return [Employee(e.id, e.name, e.fte, e.utilization_rate) for e in employees]
