# Users (Seller credentials)
sellers = {
    "admin": "123",
    "seller": "pass"
}

# Categories and items
categories = {
    "Adobo": [],
    "Sinigang": [],
    "Halo-Halo": []
}

# Customer cart
cart = []

# Seller menu
def seller_menu():
    while True:
        print("\nSeller Menu:")
        print("1. Add Item\n2. Remove Item\n3. Logout")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

# Add item to a category
def add_item():
    while True:
        print("\nAvailable Categories:")
        for category in categories:
            print(f"- {category}")

        cat = input("Choose a category (or type 'cancel' to go back): ").strip()
        if cat in categories:
            name = input("Enter item name: ").strip()
            price = input("Enter item price: ").strip()
            categories[cat].append((name, price))
            print(f"Added {name} ({price}) to {cat}.")

            cont = input("Do you want to add another item? (yes/no): ").strip().lower()
            if cont != "yes":
                break
        elif cat.lower() == "cancel":
            break
        else:
            print("Invalid category. Try again.")

# Remove item from a category
def remove_item():
    while True:
        print("\nAvailable Categories:")
        for category in categories:
            print(f"- {category}")

        cat = input("Choose a category (or type 'cancel' to go back): ").strip()
        if cat in categories and categories[cat]:
            print(f"\nItems in {cat}:")
            for i, (name, price) in enumerate(categories[cat], start=1):
                print(f"{i}. {name} - {price}")

            item_no = input("Enter item number to remove: ").strip()
            try:
                item_no = int(item_no) - 1
                if 0 <= item_no < len(categories[cat]):
                    removed = categories[cat].pop(item_no)
                    print(f"Removed {removed[0]} from {cat}.")

                    cont = input("Do you want to remove another item? (yes/no): ").strip().lower()
                    if cont != "yes":
                        break
                else:
                    print("Invalid item number. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif cat.lower() == "cancel":
            break
        else:
            print("Invalid category or no items to remove.")

# Customer menu
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Order Items\n2. View Cart\n3. Cancel")
        choice = input("Choose: ").strip()

        if choice == "1":
            order_items()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")

# Order items from a category
def order_items():
    print("\nAvailable Categories and Items:")
    for category, items in categories.items():
        print(f"\n{category}:")
        if items:
            for i, (name, price) in enumerate(items, start=1):
                print(f"{i}. {name} - {price}")
        else:
            print("No items available.")

    cat = input("Choose a category: ").strip()
    if cat in categories and categories[cat]:
        item_no = input("Enter item number to order: ").strip()
        try:
            item_no = int(item_no) - 1
            quantity = input("Enter quantity: ").strip()
            quantity = int(quantity)

            if 0 <= item_no < len(categories[cat]):
                item = categories[cat][item_no]
                cart.append((item[0], item[1], quantity))
                print(f"Added {quantity} x {item[0]} to cart.")
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid category or no items available.")

# View items in the cart
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
    while True:
        print("\n1. Print Receipt\n2. Remove Item\n3. Back")
        choice = input("Choose: ").strip()

        if choice == "1":
            print_receipt()
            break
        elif choice == "2":
            remove_from_cart()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

# Remove an item from the cart
def remove_from_cart():
    if cart:
        try:
            item_no = input("Enter item number to remove: ").strip()
            item_no = int(item_no) - 1
            if 0 <= item_no < len(cart):
                removed = cart.pop(item_no)
                print(f"Removed {removed[0]} from cart.")
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Cart is empty.")

# Print the receipt and clear the cart
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

# Main program
def main():
    while True:
        print("\nWelcome to the Kiosk System")
        print("1. Seller\n2. Customer\n3. Exit")
        user_type = input("Choose: ").strip()

        if user_type == "1":
            print("\nLogin")
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username in sellers and sellers[username] == password:
                print("Login successful!")
                seller_menu()
            else:
                print("Invalid credentials. Try again.")

        elif user_type == "2":
            customer_menu()

        elif user_type == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
