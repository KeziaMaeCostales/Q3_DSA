# Users (Seller credentials)
sellers = {
    "admin": "123",
    "seller": "pass"
}

# Categories and items
categories = {
    "Pasta": [],
    "Desserts": [],
    "Drinks": []
}

# Customer cart
cart = []

def seller_menu():
    while True:
        print("\nSeller Menu:")
        print("1. Add Item\n2. Remove Item\n3. Logout")
        choice = get_predefined_input(["1", "2", "3"], "Choose: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            print("Logging out...")
            break

def add_item():
    print("\nAvailable Categories:")
    for category in categories:
        print(f"- {category}")

    cat = get_predefined_input(categories.keys(), "Choose a category: ")
    name = "Item"  # Replace with predefined values or logic for testing
    price = "10.0"  # Replace with predefined values or logic for testing
    categories[cat].append((name, price))
    print(f"Added {name} ({price}) to {cat}.")

def remove_item():
    print("\nAvailable Categories:")
    for category in categories:
        print(f"- {category}")

    cat = get_predefined_input(categories.keys(), "Choose a category: ")
    if categories[cat]:
        print(f"\nItems in {cat}:")
        for i, (name, price) in enumerate(categories[cat], start=1):
            print(f"{i}. {name} - {price}")

        item_no = get_predefined_input(range(1, len(categories[cat]) + 1), "Enter item number to remove: ")
        removed = categories[cat].pop(int(item_no) - 1)
        print(f"Removed {removed[0]} from {cat}.")
    else:
        print("No items to remove.")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Order Items\n2. View Cart\n3. Cancel")
        choice = get_predefined_input(["1", "2", "3"], "Choose: ")

        if choice == "1":
            order_items()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            print("Returning to main menu...")
            break

def order_items():
    print("\nAvailable Categories and Items:")
    for category, items in categories.items():
        print(f"\n{category}:")
        if items:
            for i, (name, price) in enumerate(items, start=1):
                print(f"{i}. {name} - {price}")
        else:
            print("No items available.")

    cat = get_predefined_input(categories.keys(), "Choose a category: ")
    if categories[cat]:
        item_no = get_predefined_input(range(1, len(categories[cat]) + 1), "Enter item number to order: ")
        quantity = "2"  # Replace with predefined values or logic for testing

        item = categories[cat][int(item_no) - 1]
        cart.append((item[0], item[1], int(quantity)))
        print(f"Added {quantity} x {item[0]} to cart.")
    else:
        print("No items available.")

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return

    print("\nYour Cart:")
    total = 0
    for i, (name, price, quantity) in enumerate(cart, start=1):
        item_total = float(price) * quantity
        total += item_total
        print(f"{i}. {name} - {price} x {quantity} = {item_total:.2f}")

    print(f"Total: {total:.2f}")
    print("\n1. Print Receipt\n2. Remove Item\n3. Back")
    choice = get_predefined_input(["1", "2", "3"], "Choose: ")

    if choice == "1":
        print_receipt()
    elif choice == "2":
        remove_from_cart()

def remove_from_cart():
    if cart:
        item_no = get_predefined_input(range(1, len(cart) + 1), "Enter item number to remove: ")
        removed = cart.pop(int(item_no) - 1)
        print(f"Removed {removed[0]} from cart.")
    else:
        print("Cart is empty.")

def print_receipt():
    print("\nReceipt:")
    total = 0
    for name, price, quantity in cart:
        item_total = float(price) * quantity
        total += item_total
        print(f"{name} - {price} x {quantity} = {item_total:.2f}")
    print(f"Total: {total:.2f}")
    cart.clear()
    print("Thank you for your order!")

def get_predefined_input(valid_choices, prompt):
    """Simulate user input for predefined options."""
    for choice in valid_choices:
        print(f"{prompt}{choice}")  # Simulate showing options
        return str(choice)

def main():
    while True:
        print("\nWelcome to the Kiosk System")
        print("1. Seller\n2. Customer\n3. Exit")
        user_type = get_predefined_input(["1", "2", "3"], "Choose: ")

        if user_type == "1":
            print("\nLogin")
            username = "admin"  # Replace with predefined values or logic for testing
            password = "123"  # Replace with predefined values or logic for testing

            if username in sellers and sellers[username] == password:
                print("Login successful!")
                seller_menu()
            else:
                print("Invalid credentials.")

        elif user_type == "2":
            customer_menu()

        elif user_type == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
