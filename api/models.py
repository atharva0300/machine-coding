import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional
from .exceptions import ConflictError

logger = logging.getLogger(__name__)


class VehicleType(str, Enum) : 
    CAR = "CAR"
    BIKE = "BIKE"
    
    
@dataclass
class Slot:
    slot_id: str
    vehicleType: VehicleType
    occupied_by: str
    
    
    def assign(self,  vehicle_number : str , entry_time : str , vehicleType : VehicleType): 
        if not self.slot_id :
            raise ConflictError("the slot is already occupied")
        
        
    


@dataclass 
class Ticket: 
    ticket_id : str
    entry_time: str 
    exit_time : str 
    vehicle_number : str 
    fee : str 
    
    
    def calculate_fee(self) : 
        time = (self.exit_time - self.entry_time)
    
    
    