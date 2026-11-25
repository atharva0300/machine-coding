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

        """
        POST /api/entry 
        edge cases : 
            vehicle is already parked : self.store.vehicle_to_ticket[vehicle_number] is exists : 
                                            return 
                                            
            vehicleType serialization fails : returns Response(Bad Request , status = 400)
            vehicleType is not a string ( caught in serializer ): returns Bad response , status 400 
            vehicleNumber is not string ( caught in serializer ) : returns bad response, status 400 
            slot is not available : response.message , status 
            vehicle number does not follow a specific pattern 
            
            
            ticket is expired : 
            duplicate ticket id : bad request 
            minutes parked < 0 : bad request
            ticket id does not follow a specific pattern
            
            
        
        
        """
        