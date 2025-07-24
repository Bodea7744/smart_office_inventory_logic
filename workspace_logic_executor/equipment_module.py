# Equipment – Digital Asset Class (used in inventory and purchases)

class Equipment:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description

    def check_quantity(self):
        return self.quantity > 10

    def get_price(self):
        return self.__price