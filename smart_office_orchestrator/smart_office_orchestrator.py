# Smart Office Orchestrator – Central Execution Logic

from equipment_module import Equipment
from staff_member import StaffMember
from workspace_user import WorkspaceUser

# List of equipment in workspace
equipment_list = [
    Equipment("DeskStation Pro", 4500, 2, "High-performance workstation"),
    Equipment("ErgoMouse X", 200, 30, "Wireless ergonomic mouse"),
    Equipment("FlexiBoard 5", 120, 45, "RGB backlit keyboard"),
    Equipment("ViewPanel HD", 2000, 42, "Full HD office display"),
    Equipment("SoundBeam Headset", 500, 1, "Headset with microphone")
]

# List of staff members
staff = [
    StaffMember("Valentin Boca", "valentin@officenet.com", 8000, "Iasi"),
    StaffMember("Marta Ghioca", "maria.teletext.com", 12000, "Brasov")
]

# List of workspace users (access log uses equipment prices)
users = [
    WorkspaceUser("Bodea Marian", "bodea@email.com", "Iasi", "0712345678", [equipment_list[0].get_price(), equipment_list[1].get_price()]),
    WorkspaceUser("Vasilica Gherghe", "vasi@email.com", "Brasov", "0722334455", [equipment_list[2].get_price()]),
    WorkspaceUser("Mihail Mihai", "mihai.email.com", "Timisoara", "0733445566", [])
]

print("\nChecking equipment stock")
for item in equipment_list:
    print(f"{item.name}: {'Stock OK' if item.check_quantity() else 'Low stock'}")

print("\nValidating staff email addresses")
for member in staff:
    print(f"{member.name}: {'Valid email' if member.check_email() else 'Invalid email'}")

print("\nApplying 10% salary increase to first staff member")
staff[0].increase_salary(10)
print(f"{staff[0].name} - New salary: {staff[0].get_salary()} RON")

print("\nCalculating total expenses by each user")
for user in users:
    print(f"{user.name} spent: {user.total_spent()} RON")

print("\nAssigning new equipment to last user")
new_item = equipment_list[4]
users[2].add_equipment(new_item.get_price())
print(f"{users[2].name} acquired: {new_item.name} for {new_item.get_price()} RON")
print(f"{users[2].name} now spent: {users[2].total_spent()} RON")

print("\nWorkspace User Profiles")
for user in users:
    print(user.display_info())
    print()

print("Staff Member Profiles")
for member in staff:
    print(member.display_info())