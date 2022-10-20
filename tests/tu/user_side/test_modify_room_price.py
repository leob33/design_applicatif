from hostel_management.domain.model.hostel import Hostel
from hostel_management.domain.model.price import Price
from hostel_management.domain.model.room import Room
from hostel_management.domain.use_cases.modify_hostel_room_prices_use_case import ModifyHostelRoomPricesUseCase
from tests.tu.server_side.hostel_db_stub_test import HostelDbStub


def test_rdc_price_room_is_20_after_modification():
    floor = 0
    room_number = 1
    room_price = Price(50)
    hostel_room_bdd = HostelDbStub([Room(floor, room_number, room_price)])
    rdc_new_price = Price(20)
    expected_hostel = Hostel([Room(floor, room_number, rdc_new_price)])
    hostel_use_case = ModifyHostelRoomPricesUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_use_case.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_use_case.hostel == expected_hostel


def test_first_floor_room_price_is_53_5_when_rdc_price_is_50():
    floor = 1
    room_number = 1
    room_price = Price(50)
    hostel_room_bdd = HostelDbStub([Room(floor, room_number, room_price)])
    rdc_new_price = Price(50)
    expected_new_price = Price(53.5)
    expected_hostel = Hostel([Room(floor, room_number, expected_new_price)])
    hostel_use_case = ModifyHostelRoomPricesUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_use_case.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_use_case.hostel == expected_hostel


def test_second_floor_room_price_is_61_when_rdc_room_price_is_50():
    floor = 2
    room_number = 1
    room_price = Price(50)
    hostel_room_bdd = HostelDbStub([Room(floor, room_number, room_price)])
    rdc_new_price = Price(50)
    expected_new_price = Price(61)
    expected_hostel = Hostel([Room(floor, room_number, expected_new_price)])
    hostel_use_case = ModifyHostelRoomPricesUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_use_case.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_use_case.hostel == expected_hostel


def test_third_floor_room_price_is_66_5_when_rdc_room_price_is_50():
    floor = 3
    room_number = 1
    room_price = Price(50)
    hostel_room_bdd = HostelDbStub([Room(floor, room_number, room_price)])
    rdc_new_price = Price(50)
    expected_new_price = Price(66.5)
    expected_hostel = Hostel([Room(floor, room_number, expected_new_price)])
    hostel_use_case = ModifyHostelRoomPricesUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_use_case.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_use_case.hostel == expected_hostel


def test_max_room_price_is_200_for_each_floor():
    max_price = Price(200)
    room_number = 1
    hostel_room_bdd = HostelDbStub([Room(0, room_number, max_price),
                                    Room(1, room_number, max_price),
                                    Room(2, room_number, max_price),
                                    Room(3, room_number, max_price)])
    rdc_new_price = Price(210)
    expected_hostel = Hostel([Room(0, room_number, max_price),
                              Room(1, room_number, max_price),
                              Room(2, room_number, max_price),
                              Room(3, room_number, max_price)])
    hostel_use_case = ModifyHostelRoomPricesUseCase(hostel_room_bdd=hostel_room_bdd)

    hostel_use_case.update_list_of_rooms(rdc_price=rdc_new_price)

    assert hostel_use_case.hostel == expected_hostel
