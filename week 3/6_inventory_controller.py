print("===== Inventory Controller =====")

inventory = {}


def add_product(name, price, stock):
    name = name.strip()

    if not name:
        raise ValueError("Product name cannot be empty.")

    if name in inventory:
        raise ValueError("Product already exists.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    if stock < 0:
        raise ValueError("Stock cannot be negative.")

    inventory[name] = {
        "price": price,
        "stock": stock
    }


def search_product(name):
    return inventory.get(name.strip())


def update_price(name, new_price):
    if name not in inventory:
        raise ValueError("Product not found.")

    if new_price < 0:
        raise ValueError("Price cannot be negative.")

    inventory[name]["price"] = new_price


def increase_stock(name, quantity):
    if name not in inventory:
        raise ValueError("Product not found.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    inventory[name]["stock"] += quantity


def sell_product(name, quantity):
    if name not in inventory:
        raise ValueError("Product not found.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    if quantity > inventory[name]["stock"]:
        raise ValueError("Sale exceeds available stock.")

    inventory[name]["stock"] -= quantity


def calculate_total_inventory_value():
    return sum(
        product["price"] * product["stock"]
        for product in inventory.values()
    )


def low_stock_report(threshold=5):
    if threshold < 0:
        raise ValueError("Threshold cannot be negative.")

    return {
        name: product
        for name, product in inventory.items()
        if product["stock"] < threshold
    }


# Example
add_product("Laptop", 999.99, 10)
add_product("Mouse", 25.50, 3)
add_product("Keyboard", 75.00, 6)

print(search_product("Laptop"))

update_price("Mouse", 29.99)
increase_stock("Mouse", 2)
sell_product("Laptop", 2)

print("Total inventory value:",
      calculate_total_inventory_value())

print("Low-stock products:")
print(low_stock_report())

print("Low-stock products below 8 units:")
print(low_stock_report(threshold=8))
