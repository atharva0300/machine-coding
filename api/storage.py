from .models import Employee


class InMemoryStore:
    def __init__(self):
        self.employees: dict[int, Employee] = {}
        self._counter = 0

    def next_id(self) -> int:
        self._counter += 1
        return self._counter
