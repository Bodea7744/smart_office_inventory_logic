# Workspace User – Base and Standard Tier

from entity_base import Entity

class WorkspaceUser(Entity):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = {}  # Equipment → Quantity

    def add_equipment(self, equipment, quantity):
        if equipment in self.shopping_history:
            self.shopping_history[equipment] += quantity
        else:
            self.shopping_history[equipment] = quantity

    def total_spent(self):
        total = 0
        for equipment, quantity in self.shopping_history.items():
            total += equipment.get_price() * quantity
        return total

    def display_info(self):
        print(f"{self.name} – Phone: {self.phone}, Email: {self._email}")
        print(f"Total spent: {self.total_spent()} RON")

class StandardWorkspaceUser(WorkspaceUser):
    def calculate_discount(self):
        spent = self.total_spent()
        return 10 if spent > 10000 else 5

    def display_info(self):
        super().display_info()
        print(f"Applicable discount: {self.calculate_discount()}%")