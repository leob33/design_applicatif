from hostel_management.domain.model.hostel import Hostel
from hostel_management.domain.model.price import Price
from hostel_management.domain.model.room import Room
from hostel_management.domain.repository.hotel_repository import HotelRepository


class HotelRepositoryHardCoded(HotelRepository):
    """
    une classe bidon qui implémente l'interface, c dans ce dossier que cela va, c le côté droit,
    hors du domaine / hexagone
    """

    def get_hostel(self) -> Hostel:
        rooms = [Room(0, 1, Price(120)),
                 Room(1, 1, Price(120)),
                 Room(2, 1, Price(120)),
                 Room(3, 1, Price(120))]

        return Hostel(rooms=rooms)
