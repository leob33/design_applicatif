from hostel_management.domain.model.hostel import Hostel
from hostel_management.domain.repository.hotel_repository import HotelRepository
from hostel_management.domain.model.room import Room


class HostelDbStub(HotelRepository):

    def __init__(self, list_of_rooms: list[Room]):
        self._list_of_rooms = list_of_rooms

    def get_hostel(self) -> Hostel:
        return Hostel(rooms=self._list_of_rooms)
