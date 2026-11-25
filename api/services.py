import logging
import threading
from datetime import date
from decimal import Decimal

from .exceptions import ConflictError
from .models import Department, Employee
from .storage import InMemoryStore

logger = logging.getLogger(__name__)


class EmployeeService:
    def __init__(self, store: InMemoryStore):
        self.store = store
        self._lock = threading.Lock()

    def create_employee(self, name: str, email: str, department: str, designation: str,
                        salary: Decimal, joining_date: date) -> Employee:
        email = email.strip().lower()
        with self._lock:
            if any(e.email == email for e in self.store.employees.values()):
                raise ConflictError(f"Employee with email {email} already exists")
            employee = Employee(
                self.store.next_id(), name.strip(), email, Department(department),
                designation.strip(), salary, joining_date,
            )
            self.store.employees[employee.employee_id] = employee
        logger.info("Employee created id=%s email=%s", employee.employee_id, email)
        return employee
