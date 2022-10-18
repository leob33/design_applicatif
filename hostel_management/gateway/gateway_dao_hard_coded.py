from hostel_management.domain.model.hostel import Hostel
from hostel_management.domain.repository.hotel_repository import HotelRepository


class HotelRepositoryHardCoded(HotelRepository):
    """
    une classe bidon qui implémente l'interface, c dans ce dossier que cela va, c le côté droit,
    hors du domaine / hexagone
    """

    def get_hostel(self) -> Hostel:
        pass

    def list_hostel_rooms(self) -> list[dict]:
        raise NotImplementedError()
