# Equipment Class – office inventory item

class Equipment:
    def __init__(self, name, price, quantity, description):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.description = str(description)

    def check_stock(self):
        return self.quantity >= 10