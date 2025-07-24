# Smart Office Inventory Manager – operational script

from equipment_class import Equipment
from staff_class import Staff
from workspace_user_class import WorkspaceUser

# Equipment in office system
equipment_list = [
    Equipment("DeskStation Pro", 4500, 2, "High-performance workstation"),
    Equipment("ErgoMouse X", 200, 30, "Precision ergonomic mouse"),
    Equipment("FlexiBoard 5", 120, 45, "Backlit mechanical keyboard"),
    Equipment("ViewPanel HD", 2000, 42, "Full HD display panel"),
    Equipment("SoundBeam Headset", 500, 1, "Noise-canceling headset with mic")
]

# Office staff
staff_list = [
    Staff("Valentin Boca", "valentin@officenet.com", 8000, "Iasi"),
    Staff("Marta Ghioca", "maria.teletext.com", 12000, "Brasov")
]

# Platform users
user_list = [
    WorkspaceUser("Bodea Marian", "bodea123", "0712345678", "Iasi", [equipment_list[0], equipment_list[1]], "bodea@email.com"),
    WorkspaceUser("Vasilica Gherghe", "vasilica1341", "0722334455", "Brasov", [equipment_list[2]], "vasi@email.com"),
    WorkspaceUser("Mihail Mihai", "radu252452", "0733445566", "Timisoara", [], "mihai.email.com")
]

print("\nChecking equipment stock")
for item in equipment_list:
    print(f"{item.name}: {'Stock OK' if item.check_stock() else 'Low stock'}")

print("\nValidating staff emails")
for staff in staff_list:
    print(f"{staff.name}: {'Valid email' if staff.check_email() else 'Invalid email'}")

print("\nApplying salary increase of 10% for first staff member")
staff_list[0].increase_salary(10)
print(f"{staff_list[0].name} – Updated salary: {staff_list[0].salary} RON")

print("\nCalculating total expenditure per user")
for user in user_list:
    print(f"{user.name} spent: {user.total_spent()} RON")

print("\nAssigning new equipment to last user")
new_item = equipment_list[4]
user_list[2].add_equipment(new_item)
print(f"{user_list[2].name} acquired: {new_item.name} for {new_item.price} RON")
print(f"{user_list[2].name} total spent: {user_list[2].total_spent()} RON")