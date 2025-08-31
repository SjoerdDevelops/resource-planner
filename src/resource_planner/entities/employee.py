from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    id: Optional[int]
    name: str
    fte: float
    utilization_rate: float


def create_employee(name: str, fte: float, utilization_rate: float) -> Employee:
    return Employee(None, name, fte, utilization_rate)
