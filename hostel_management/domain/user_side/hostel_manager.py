from hostel_management.domain.application.room import Room
from hostel_management.domain.server_side.interface_hostel_data_source import InterfaceHostelDataSource


class HostelManager:
    def __init__(self, hostel_room_bdd: InterfaceHostelDataSource):
        self.hostel_room_bdd = hostel_room_bdd
        self.list_of_rooms = [Room(floor=room['étage'], price=room['prix'], number=room['numéro']) for room in
                              self.hostel_room_bdd.list_hostel_rooms()]

    def update_list_of_rooms(self, rdc_price: float) -> None:
        for room in self.list_of_rooms:
            room.update_price(rdc_price)
