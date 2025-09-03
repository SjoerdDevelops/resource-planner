import pytest
from peewee import SqliteDatabase
from infrastructure.models.employee_model import EmployeeModel
from infrastructure.repositories.db_employee_repository import (
    DBEmployeeRepository,
)

from domain.entities.employee import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)

# Use an in-memory SQLite database for testing
test_db = SqliteDatabase(":memory:")


@pytest.fixture(scope="function")
def setup_db():
    """Setup and teardown the in-memory database for each test."""
    EmployeeModel._meta.database = test_db
    test_db.bind([EmployeeModel])
    test_db.connect()
    test_db.create_tables([EmployeeModel])
    yield
    test_db.drop_tables([EmployeeModel])
    test_db.close()


@pytest.fixture
def sample_employee() -> Employee:
    """Return a sample Employee object."""
    return Employee(
        PersonalInfo(name="Alice", surname="Smith"),
        EmploymentDetails(fte=1.0, utilization_rate=0.8),
        CompanyCredentials(username="asmith", acronym="AS"),
    )


def test_add_employee(setup_db, sample_employee):
    store = DBEmployeeRepository()
    added_employee = store.add(sample_employee)

    assert isinstance(added_employee, Employee)
    assert added_employee.personal.name == "Alice"
    assert added_employee.personal.surname == "Smith"
    assert added_employee.employment.fte == 1.0
    assert added_employee.credentials.username == "asmith"


def test_get_by_id(setup_db, sample_employee):
    store = DBEmployeeRepository()
    added_employee = store.add(sample_employee)
    employee_id = EmployeeModel.get(EmployeeModel.username == "asmith").id

    fetched_employee = store.get_by_id(employee_id)
    assert fetched_employee is not None
    assert fetched_employee.credentials.username == "asmith"


def test_update_employee(setup_db, sample_employee):
    store = DBEmployeeRepository()
    store.add(sample_employee)

    updated_employee = Employee(
        PersonalInfo(name="Alice", surname="Johnson"),
        EmploymentDetails(fte=0.9, utilization_rate=0.95),
        CompanyCredentials(username="asmith", acronym="AJ"),
    )
    rows_modified = store.update("asmith", updated_employee)
    assert rows_modified == 1

    fetched_employee = store.get_by_id(
        EmployeeModel.get(EmployeeModel.username == "asmith").id
    )
    assert fetched_employee is not None
    assert fetched_employee.personal.surname == "Johnson"
    assert fetched_employee.employment.fte == 0.9
    assert fetched_employee.credentials.acronym == "AJ"


def test_list_all_employees(setup_db, sample_employee):
    store = DBEmployeeRepository()
    store.add(sample_employee)

    employee2 = Employee(
        PersonalInfo(name="Bob", surname="Brown"),
        EmploymentDetails(fte=0.5, utilization_rate=0.6),
        CompanyCredentials(username="bbrown", acronym="BB"),
    )
    store.add(employee2)

    all_employees = store.list_all()
    assert len(all_employees) == 2
    usernames = [e.credentials.username for e in all_employees]
    assert "asmith" in usernames
    assert "bbrown" in usernames
