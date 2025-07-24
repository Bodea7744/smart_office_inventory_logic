# Smart Office Supply Analysis

# Initial product sales data in a digital workspace inventory
sales = {
    "DeskStation Pro": 15,
    "ErgoMouse X": 150,
    "FlexiBoard 5": 85,
    "ViewPanel HD": 30,
    "CableConnect Plus": 200
}
print(f"Initial inventory data: {sales}")

# a) Total units sold across all items
total_sales = sum(sales.values())
print(f"Total units sold: {total_sales}")

# b) Most sold product in the inventory
top_selling = max(sales, key=sales.get)
print(f"Top-selling product: {top_selling}")

# c) Least sold product
low_selling = min(sales, key=sales.get)
print(f"Least-selling product: {low_selling}")

# d) Check if "WebVision Cam" exists; if not, add with 0 units
if "WebVision Cam" not in sales:
    sales["WebVision Cam"] = 0
    print("Product 'WebVision Cam' added to inventory with initial quantity 0.")
else:
    print("Product 'WebVision Cam' already present in inventory.")

# e) Correction: Increase ViewPanel HD sales by 5 units
sales["ViewPanel HD"] += 5
print("Quantity adjusted: 'ViewPanel HD' incremented by 5 units.")

# Summary of updated inventory
print("\nUpdated inventory data:", sales)
print(f"New total units sold: {sum(sales.values())}")
print(f"Updated top-seller: {max(sales, key=sales.get)}")
print(f"Updated low-seller: {min(sales, key=sales.get)}")
print(f"'WebVision Cam' sold?: {'Yes' if sales['WebVision Cam'] > 0 else 'No'}")

# Function to identify products with critical sales levels (<50 units)
def get_critical_stock(sales_data):
    return [item for item, qty in sales_data.items() if qty < 50]

critical_items = get_critical_stock(sales)
print("\nCritical stock items (below threshold):", critical_items)

# Function to verify data integrity (no negative values)
def is_data_valid(sales_data):
    return all(qty >= 0 for qty in sales_data.values())

if is_data_valid(sales):
    print("Inventory data check passed: all quantities are non-negative.")
else:
    print("Warning: Inventory contains invalid (negative) quantities.")