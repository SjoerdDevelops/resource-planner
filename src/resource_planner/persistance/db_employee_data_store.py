from resource_planner.domain.employee_data_store import EmployeeDataStore
from peewee import SqliteDatabase, Model, CharField, IntegerField, DoubleField
from typing import Optional, List, Any
from resource_planner.domain.employee import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from pydantic import BaseModel, ValidationError, ConfigDict


db = SqliteDatabase("database.db")


# TODO: Enforce acceptable values for the database entries
# TODO: Split the database model into seperate models
class EmployeeModel(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    surname = CharField()
    fte = DoubleField()
    utilization_rate = DoubleField()
    username = CharField(unique=True)
    acronym = CharField(unique=True)

    class Meta:
        database = db


class EmployeeSchema(BaseModel):
    id: int
    name: str
    surname: str
    fte: float
    utilization_rate: float
    username: str
    acronym: str

    model_config = ConfigDict(from_attributes=True)


db.create_tables([EmployeeModel])


def parse_employee(data: Any) -> Optional[Employee]:
    try:
        employee: EmployeeSchema = EmployeeSchema.model_validate(data)
        return create_employee_from_schema(employee)
    except ValidationError as e:
        print("Validation failed:", e.json())
        return None


def create_employee_from_schema(employeeSchema: EmployeeSchema) -> Employee:
    return Employee(
        PersonalInfo(employeeSchema.name, employeeSchema.surname),
        EmploymentDetails(employeeSchema.fte, employeeSchema.utilization_rate),
        CompanyCredentials(employeeSchema.username, employeeSchema.acronym),
    )


# TODO: Add @override method from typing when using python >3.12
class DBEmployeeDataStore(EmployeeDataStore):
    def get_by_id(self, id: int) -> Optional[Employee]:
        row = EmployeeModel.get_or_none(EmployeeModel.id == id)
        return parse_employee(row)

    def add(self, employee: Employee) -> Employee:
        row = EmployeeModel.create(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        )
        return create_employee_from_schema(EmployeeSchema.model_validate(row))

    def update(self, username: str, employee: Employee) -> int:
        query = EmployeeModel.update(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        ).where(EmployeeModel.username == username)

        rows_modified = query.execute()
        return rows_modified

    def list_all(self) -> List[Employee]:
        return [
            employee
            for row in EmployeeModel.select()
            if (employee := parse_employee(row)) is not None
        ]
