from dataclasses import dataclass


@dataclass
class Room:
    floor: int
    number: int
    price: float

    def update_price(self, rdc_price: float):
        if self.floor == 0:
            self.price = rdc_price
        elif self.floor == 1:
            self.price = rdc_price * 1.07
        elif self.floor == 2:
            self.price = rdc_price * 1.22
        elif self.floor == 3:
            self.price = rdc_price * 1.33
        if self.price > 200:
            self.price = 200