from abc import ABCMeta, abstractmethod

from hostel_management.domain.model.hostel import Hostel


class HotelRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_hostel(self) -> Hostel:
        ...
