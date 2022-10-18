from hostel_management.hostel_bdd import HostelDB
from hostel_management.domain.user_side.hostel_manager import HostelManager
from hostel_management.domain.application.room import Room
from tests.tu.server_side.hostel_db_stub_test import HostelDbStubRdcTest, HostelDbStubFirstFloorTest, \
    HostelDbStubSecondFloorTest, HostelDbStubThirdFloorTest, HostelDbStubRoomMax200Test


def test_list_rooms_returns_list_of_rooms():
    expected_list_of_rooms = [
        Room(0, 1, 50),
        Room(1, 1, 50),
        Room(2, 1, 50),
        Room(3, 1, 50),
    ]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDB())
    list_of_rooms = hostel_manager.list_of_rooms

    assert list_of_rooms == expected_list_of_rooms


def test_rdc_price_room():
    rdc_price = 20
    expected_list_of_rooms = [Room(0, 1, rdc_price)]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDbStubRdcTest())
    hostel_manager.update_list_of_rooms(rdc_price=rdc_price)

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_1er_etage_room():
    rdc_price = 50
    expected_list_of_rooms = [Room(1, 1, rdc_price * 1.07),
                              Room(0, 1, rdc_price)]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDbStubFirstFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=rdc_price)

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_2eme_etage_room():
    rdc_price = 50
    expected_list_of_rooms = [Room(2, 1, rdc_price * 1.22)]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDbStubSecondFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=rdc_price)

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_3eme_etage_room():
    rdc_price = 50
    expected_list_of_rooms = [Room(3, 1, rdc_price * 1.33)]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDbStubThirdFloorTest())
    hostel_manager.update_list_of_rooms(rdc_price=rdc_price)

    assert hostel_manager.list_of_rooms == expected_list_of_rooms


def test_max_room_price():
    rdc_price = 200
    expected_list_of_rooms = [
        Room(0, 1, rdc_price),
        Room(3, 1, 200)
    ]

    hostel_manager = HostelManager(hostel_room_bdd=HostelDbStubRoomMax200Test())
    hostel_manager.update_list_of_rooms(rdc_price=rdc_price)

    assert hostel_manager.list_of_rooms == expected_list_of_rooms
