class Price:

    def __init__(self, value: float):
        self._value = value

    def calculate_price(self, percentage: float) -> 'Price':
        new_price = Price(value=self._value * (1 + percentage / 100))
        if new_price._value > 200:
            new_price = Price(200)
        return new_price

    def __eq__(self, other):
        if self._value == other._value:
            return True
        else:
            return False