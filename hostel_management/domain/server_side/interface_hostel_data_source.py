from abc import ABCMeta, abstractmethod


class InterfaceHostelDataSource(metaclass=ABCMeta):

    @abstractmethod
    def list_hostel_rooms(self) -> list[dict]:
        ...