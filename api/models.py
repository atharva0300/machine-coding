from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class Department(str, Enum):
    ENGINEERING = "ENGINEERING"
    HR = "HR"
    FINANCE = "FINANCE"
    SALES = "SALES"


@dataclass
class Employee:
    employee_id: int
    name: str
    email: str
    department: Department
    designation: str
    salary: Decimal
    joining_date: date
