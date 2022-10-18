from hostel_management.domain.server_side.interface_hostel_data_source import InterfaceHostelDataSource


class HostelDB(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 0, 'numéro': 1, 'prix': 50},
            {'étage': 1, 'numéro': 1, 'prix': 50},
            {'étage': 2, 'numéro': 1, 'prix': 50},
            {'étage': 3, 'numéro': 1, 'prix': 50},
        ]
        return hostel_rooms_list
