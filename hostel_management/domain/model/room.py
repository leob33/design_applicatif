from dataclasses import dataclass

from hostel_management.domain.model.price import Price


@dataclass
class Room:
    floor: int
    number: int
    price: Price

    def update_price(self, rdc_price: Price):
        if self.floor == 0:
            self.price = rdc_price.calculate_price(0)
        elif self.floor == 1:
            self.price = rdc_price.calculate_price(7)
        elif self.floor == 2:
            self.price = rdc_price.calculate_price(22)
        elif self.floor == 3:
            self.price = rdc_price.calculate_price(33)
