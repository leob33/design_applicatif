from hostel_management.domain.model.price import Price
from hostel_management.domain.repository.hotel_repository import HotelRepository


class ModifyHostelRoomPricesUseCase:
    def __init__(self, hostel_room_bdd: HotelRepository):
        self.hostel = hostel_room_bdd.get_hostel()

    def update_list_of_rooms(self, rdc_price: Price) -> None:
        self.hostel.update_room_prices(rdc_price=rdc_price)
