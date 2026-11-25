import logging
import threading

from .exceptions import ConflictError, DomainError
from .storage import InMemoryStore

logger = logging.getLogger(__name__)


class Service:
    def __init__(self, store: InMemoryStore):
        self.store = store
        self._lock = threading.Lock()
