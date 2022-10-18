from hostel_management.domain.model.price import Price
from hostel_management.domain.model.room import Room


class Hostel:
    def __init__(self, rooms: list[Room]):
        self._rooms = rooms

    def update_room_prices(self, rdc_price: Price) -> None:
        for room in self._rooms:
            room.update_price(rdc_price=rdc_price)

    def __eq__(self, other: 'Hostel') -> bool:
        is_equal = True
        for self_room, other_room in zip(self._rooms, other._rooms):
            if self_room != other_room:
                is_equal = False
                break
        return is_equal


