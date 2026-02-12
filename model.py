from dataclasses import dataclass, field
from datetime import datetime
from abc import ABC,abstractmethod
# ClassVar 是说这个变量是Class级别的，不是对象级别的
from typing import ClassVar


# =========================
# Base Entity
# =========================
# ABC 不是用于实例化，而是用于被继承，如果有abstractmethod，不可以实例化，没有的话，可以正常实例化
@dataclass
class Entity(ABC):
    id: str
    created_at: datetime

    # 因为class 属性有逻辑要处理，所以需要post_init, 如果只是赋值，则不需要post_init
    def __post_init__(self):
        if not self.id:
            raise ValueError("id must be a non-empty string")
        
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


# =========================
# Bike
# =========================
@dataclass
class Bike(Entity):
    bike_type: str
    # repr false，只影响__repr__的打印， 可选参数，_内部变量，用property读取，用setter增加逻辑
    _status: str = field(repr=False)

    # 如果没有ClassVar，它则是实例化的变量，但这里它需要是Class级别的
    VALID_TYPES: ClassVar[tuple[str, ...]] = ("classic", "electric")
    VALID_STATUSES: ClassVar[tuple[str, ...]] = (
        "available",
        "in_use",
        "maintenance",
    )

    def __post_init__(self):
        super().__post_init__()

        if self.bike_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid bike_type: {self.bike_type}")

        self.status = self._status  # 通过 setter 校验

    # -------- status property --------
    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {value}")
        self._status = value
    # 因为父类中，有逻辑需要执行，所以这个这里也需要继承下来
    def __str__(self):
        return f"Bike({self.id}, {self.bike_type}, {self.status})"

    def __repr__(self):
        return (
            f"Bike(id={self.id!r}, "
            f"bike_type={self.bike_type!r}, "
            f"status={self.status!r})"
        )


# =========================
# Classic Bike
# =========================
@dataclass
class ClassicBike(Bike):
    gear_count: int = 7

    # 因为父类中，有逻辑需要执行，所以这个这里也需要继承下来
    def __post_init__(self):
        super().__post_init__()

        if self.gear_count <= 0:
            raise ValueError("gear_count must be positive")

        if self.bike_type != "classic":
            self.bike_type = "classic"

    def __str__(self):
        return f"Your ClassicBike({self.id}, gears={self.gear_count}) has been successfully created in system, und it is {self._status}.!"


# =========================
# Electric Bike
# =========================
@dataclass
class ElectricBike(Bike):
    battery_level: float = 100.0
    max_range_km: float = 50.0

    def __post_init__(self):
        super().__post_init__()

        if not (0 <= self.battery_level <= 100):
            raise ValueError("battery_level must be between 0 and 100")

        if self.max_range_km <= 0:
            raise ValueError("max_range_km must be positive")

        if self.bike_type != "electric":
            self.bike_type = "electric"

    def __str__(self):
        return (
            f"ElectricBike({self.id}, "
            f"battery={self.battery_level}%)"
        )


# =========================
# Station
# =========================
@dataclass
class Station(Entity):
    name: str
    capacity: int
    latitude: float
    longitude: float

    def __str__(self):
        return f"Station({self.name}, capacity={self.capacity})"


# =========================
# User
# =========================
@dataclass
class User(Entity):
    name: str
    email: str
    user_type: str

    VALID_TYPES: ClassVar[tuple[str, ...]] = ("casual", "member")

    def __post_init__(self):
        super().__post_init__()

        if self.user_type not in self.VALID_TYPES:
            raise ValueError("Invalid user_type")

    def __str__(self):
        return f"User({self.name}, type={self.user_type} has been created)"

# =========================
# test user und bike object creating
# =========================
# user01 = User(1,datetime.now(),"Anna", "xxx@xxx","member")
# print(user01)
 
# bike01 = ClassicBike(1,datetime.now,"classic","available",8)
# print(bike01)

