from hostel_management.domain.model.room import Room
from hostel_management.domain.model.price import Price
from hostel_management.domain.repository.hotel_repository import HotelRepository


class HostelUseCase:
    def __init__(self, hostel_room_bdd: HotelRepository):
        self.hostel_room_bdd = hostel_room_bdd
        self.hostel = self.hostel_room_bdd.get_hostel()

    def update_list_of_rooms(self, rdc_price: Price) -> None:
        self.hostel.update_room_prices(rdc_price=rdc_price)
