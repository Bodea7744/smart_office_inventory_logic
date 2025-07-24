# Smart Office Supply Monitor

from stock_metrics import (
    total_units_sold,
    top_selling_product,
    lowest_selling_product,
    register_item_if_absent,
    update_item_quantity,
    get_low_stock_items,
    validate_inventory_data,
    get_item_sales
)

# Initial inventory data
inventory = {
    "DeskStation Pro": 15,
    "ErgoMouse X": 150,
    "FlexiBoard 5": 85,
    "ViewPanel HD": 30,
    "CableConnect Plus": 200
}

# Add missing item to inventory if not present
if register_item_if_absent(inventory, "WebVision Cam"):
    print("Item 'WebVision Cam' was added to inventory with a quantity of 0.")
else:
    print("Item 'WebVision Cam' is already present.")

# Apply correction to existing item
update_item_quantity(inventory, "ViewPanel HD", 5)
print("Item 'ViewPanel HD' has been updated with +5 units.")

# Validate current inventory data
if validate_inventory_data(inventory):
    print("All inventory data is valid.")
else:
    print("Warning: Issues found in inventory data.")

# Attempt access to missing item for test
print("Quantity for 'AirScan Pro':", get_item_sales(inventory, "AirScan Pro"))

# Summary of inventory statistics
print("Total units sold:", total_units_sold(inventory))
print("Top-selling item:", top_selling_product(inventory))
print("Lowest-selling item:", lowest_selling_product(inventory))
print("Items with low stock (<50 units):", get_low_stock_items(inventory))