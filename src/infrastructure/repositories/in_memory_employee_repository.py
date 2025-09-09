from application.interfaces import EmployeeRepository
from domain.entities import Employee
from uuid import UUID


class InMemoryEmployeeRepository(EmployeeRepository):
    def __init__(self) -> None:
        self._employees: list[Employee] = []

    def find_by_id(self, id: UUID) -> Employee | None:
        return next((e for e in self._employees if e.id == id), None)

    def find_by_username(self, username: str) -> Employee | None:
        return next(
            (e for e in self._employees if e.credentials.username == username), None
        )

    def find_by_acronym(self, acronym: str) -> Employee | None:
        return next(
            (e for e in self._employees if e.credentials.acronym == acronym), None
        )

    def add(self, employee: Employee) -> Employee | None:
        self._employees.append(employee)

    def remove(self, id: UUID) -> None:
        employee = next(
            (employee for employee in self._employees if employee.id == id), None
        )
        if employee:
            self._employees.remove(employee)
        else:
            raise ValueError(f"Cannot remove employee with id {id}")

    def update(self, employee: Employee) -> None:
        for index, existing in enumerate(self._employees):
            if existing.id == employee.id:
                self._employees[index] = employee
                return
        raise ValueError(f"Employee with id {employee.id} not found")

    def list_all(self) -> list[Employee]:
        # Return a copy to prevent outside mutations
        return list(self._employees)

    def clear(self) -> None:
        self._employees = []

    def reset(self, employees: list[Employee]) -> None:
        # Store a copy to prevent outside mutations
        self._employees = list(employees)
