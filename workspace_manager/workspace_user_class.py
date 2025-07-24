# WorkspaceUser Class – internal system user or platform client

class WorkspaceUser:
    def __init__(self, name, username, phone, location, inventory_access, email):
        self.name = str(name)
        self.username = str(username)
        self.phone = str(phone)
        self.location = str(location)
        self.inventory_access = list(inventory_access)
        self.email = str(email)

    def check_email(self):
        return "@" in self.email

    def total_spent(self):
        return sum(item.price for item in self.inventory_access)

    def add_equipment(self, item):
        self.inventory_access.append(item)