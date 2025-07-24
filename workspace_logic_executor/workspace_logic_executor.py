# Workspace Execution Script – Staff & Equipment Logic

from equipment_module import Equipment
from workspace_user_roles import WorkspaceUser, StandardWorkspaceUser
from staff_roles import Staff, ContractStaff, FreelanceStaff

# Equipment inventory
equipment_list = [
    Equipment("Wi-Fi Router", 220, 7, "Home network router"),
    Equipment("USB Keyboard", 120, 12, "Standard office keyboard")
]

# Workspace users
users = {
    StandardWorkspaceUser("Ana Vasiliu", "ana@email.com", "Str. Berbec 7", "0778787878"),
    WorkspaceUser("Ionela Popa", "ionela@email.com", "Str. Avarului 10", "0744555666")
}

# Staff members
employees = {
    Staff("Vlad Popa", "popa@firma.com", "Str. Popei 3", 7000, 0),
    FreelanceStaff("Maria Dinu", "maria@free.com", "Str. Pădurii 11", 6000, 0, 2),
    ContractStaff("Alexandra Ilie", "alexa@firma.com", "Str. Plopilor 21", 8500, 0, "2025-12-31")
}

# Register user
new_user = StandardWorkspaceUser("Elena Gherghe", "gherghe@email.com", "Str. Fag 14", "0733999888")
if new_user.check_email():
    users.add(new_user)
    print("USER SUCCESSFULLY REGISTERED.")

# Login check
ana = next(u for u in users if u.name == "Ana Vasiliu")
ana.set_password("vas567")
if ana.check_login("ana@email.com", "vas567"):
    print("LOGIN SUCCESSFUL:", ana.name)

# Purchase equipment
product = equipment_list[0]
ana.add_equipment(product, 1)

# Display user info
print("\nUSER ACCOUNT")
ana.display_info()

# Check working hours
for e in employees:
    e.checkin()
    e.checkout()

top_employee = max(employees, key=lambda e: e.get_working_hours())
top_employee.increase_salary(50)

print("\nWORK ANALYSIS")
print("MOST ACTIVE EMPLOYEE:", top_employee.name)
print("UPDATED SALARY:", top_employee.get_salary())

# Add new equipment
try:
    new_product = Equipment("Optical Mouse", 85, 25, "Standard USB mouse")
    if new_product.get_price() > 0:
        equipment_list.append(new_product)
        print("NEW PRODUCT ADDED.")
    else:
        raise ValueError
except:
    print("ERROR ADDING PRODUCT.")