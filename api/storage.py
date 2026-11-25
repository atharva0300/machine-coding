import logging
from typing import Optional

logger = logging.getLogger(__name__)


class InMemoryStore:
    def __init__(self):
        self._counter = 0
        
        self.vehicle_to_ticket : List[str , str]
        

    def next_id(self) -> int:
        self._counter += 1
        return self._counter
