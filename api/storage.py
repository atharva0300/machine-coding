import logging
from typing import Optional

logger = logging.getLogger(__name__)


class InMemoryStore:
    def __init__(self):
        self._counter = 0

    def next_id(self) -> int:
        self._counter += 1
        return self._counter
