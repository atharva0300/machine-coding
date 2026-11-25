import logging
import math
import threading
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from .exceptions import ConflictError, DomainError, NotFoundError, ValidationFailed
from .storage import InMemoryStore

logger = logging.getLogger(__name__)


class Service:
    def __init__(self, store: InMemoryStore):
        self.store = store
        self._lock = threading.Lock()
