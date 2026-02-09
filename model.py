from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Entity(ABC):
    def __init__(self, shared_id: str, created_at: datetime):
        self.shared_id = shared_id
        self.created_at = created_at
    
    @abstractmethod
    def __str__(self):
        pass    #>>>>>?????????????

    def __repr__(self):
        pass   #>>>>>?????????????

@dataclass
class Bike(Entity):
    bike_id: str
    bike_type: str
    status: "available"|"in_use" |"maintenance"

    def __str__(self):
        pass #>>>>>?????????????

    def __repr__(self):
        pass #>>>>>?????????????

@dataclass
class Station(Entity):
    station_id: str
    name: str
    capacity: int
    latitude: float
    longitude: float

    def __str__(self):
        pass #>>>>>?????????????

    def __repr__(self):
        pass #>>>>>?????????????

@dataclass
class User(Entity):
    user_id: str
    name: str
    email: str
    user_type: "casual"|"member"
    
    def __str__(self):
        pass #>>>>>?????????????

    def __repr__(self):
        pass #>>>>>?????????????

#????????????? no __str__, no problem
@dataclass
class CasualUser(User):
     day_pass_count: int = 0

@dataclass
class MemberUser(User):
    membership_start: datetime
    membership_end: datetime
    tier:"basic"|"premium"

@dataclass
class Trip():
    trip_id: str
    user: str
    bike: str
    start_station: str
    end_station: str
    start_time: datetime
    end_time: datetime
    distance_km: float
  
@dataclass
class MaintenanceRecord: 
    record_id:str
    bike:str
    date:datetime
    maintenance_type:str
    cost:float
    description:str

# @dataclass
# calss BikeShareSystem:  ？？要干嘛