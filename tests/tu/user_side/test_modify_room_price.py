from hostel_management.domain.model.hostel import Hostel
from hostel_management.domain.model.price import Price
from hostel_management.domain.model.room import Room
from hostel_management.domain.use_cases.hostel_use_case import HostelUseCase
from tests.tu.server_side.hostel_db_stub_test import HostelDbStub


def test_rdc_price_room():
    floor = 0
    room_number = 1
    room_price = Price(50)
    hostel_room_bdd = HostelDbStub([Room(floor, room_number, room_price)])
    rdc_new_price = Price(20)
    expected_hostel = Hostel([Room(floor, room_number, rdc_new_price)])
    hostel_manager = HostelUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_manager.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_manager.hostel == expected_hostel


def test_1er_etage_room():
    rdc_price = 50
    expected_list_of_rooms = Hostel([Room(1, 1, Price(rdc_price * 1.07))])

    hostel_manager = HostelUseCase(hostel_room_bdd=HostelDbStubFirstFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=Price(rdc_price))

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_2eme_etage_room():
    rdc_price = 50
    expected_list_of_rooms = [Room(2, 1, Price(rdc_price * 1.22))]

    hostel_manager = HostelUseCase(hostel_room_bdd=HostelDbStubSecondFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=Price(rdc_price))

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_3eme_etage_room():
    rdc_price = 50
    expected_list_of_rooms = [Room(3, 1, Price(rdc_price * 1.33))]

    hostel_manager = HostelUseCase(hostel_room_bdd=HostelDbStubThirdFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=Price(rdc_price))

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_max_room_price():
    rdc_price = 200
    expected_list_of_rooms = [
        Room(0, 1, Price(rdc_price)),
        Room(3, 1, Price(200))
    ]

    hostel_manager = HostelUseCase(hostel_room_bdd=HostelDbStubRoomMax200Test())
    hostel_manager.update_list_of_rooms(rdc_price=Price(rdc_price))

    assert hostel_manager.list_of_rooms == expected_list_of_rooms
