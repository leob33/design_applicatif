from hostel_management.domain.server_side.interface_hostel_data_source import InterfaceHostelDataSource


class HostelDbStubRdcTest(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 0, 'numéro': 1, 'prix': 50}]
        return hostel_rooms_list


class HostelDbStubFirstFloorTest(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 1, 'numéro': 1, 'prix': 20},
            {'étage': 0, 'numéro': 1, 'prix': 20},
        ]
        return hostel_rooms_list


class HostelDbStubSecondFloorTest(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 2, 'numéro': 1, 'prix': 20},
        ]
        return hostel_rooms_list


class HostelDbStubThirdFloorTest(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 3, 'numéro': 1, 'prix': 20},
        ]
        return hostel_rooms_list


class HostelDbStubRoomMax200Test(InterfaceHostelDataSource):
    def list_hostel_rooms(self) -> list[dict]:
        hostel_rooms_list = [
            {'étage': 0, 'numéro': 1, 'prix': 20},
            {'étage': 3, 'numéro': 1, 'prix': 20},
        ]
        return hostel_rooms_list