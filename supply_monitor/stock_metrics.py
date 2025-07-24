# Smart Office Supply Metrics

# Calculates total units sold from inventory data
def total_units_sold(inventory):
    return sum(inventory.values())

# Returns product with highest quantity sold (using lambda)
def top_selling_product(inventory):
    return max(inventory, key=lambda item: inventory[item])

# Returns product with lowest quantity sold (using lambda)
def lowest_selling_product(inventory):
    return min(inventory, key=lambda item: inventory[item])

# Returns quantity sold for a specific product, with error handling
def get_item_sales(inventory, item_name):
    try:
        return inventory[item_name]
    except KeyError:
        print(f"Error: '{item_name}' not found in inventory.")
        return 0

# Adds missing product entry with optional default value (0)
def register_item_if_absent(inventory, item_name, default_value=0):
    if item_name not in inventory:
        inventory[item_name] = default_value
        return True
    return False

# Adjusts unit count for a given item by a specified amount
def update_item_quantity(inventory, item_name, adjustment):
    if item_name in inventory:
        inventory[item_name] += adjustment

# Returns list of items with quantity below threshold
def get_low_stock_items(inventory, threshold=50):
    return [item for item, quantity in inventory.items() if quantity < threshold]

# Validates inventory quantities (must be between 0 and 100,000)
def validate_inventory_data(inventory):
    is_valid = True
    for item, quantity in inventory.items():
        if quantity < 0:
            print(f"Error: '{item}' has negative stock ({quantity}).")
            is_valid = False
        elif quantity > 100000:
            print(f"Warning: '{item}' has unusually high stock ({quantity}).")
            is_valid = False
    return is_valid