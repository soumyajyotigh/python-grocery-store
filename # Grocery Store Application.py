# Grocery Store Application

# Dictionary of grocery items (item: price)
grocery_items = {
    "Wheat": 40,
    "Milk": 30,
    "Sugar": 45,
    "Oil": 120,
    "Eggs": 6,
    "Bread": 25,
    "Butter": 60,
    "Cheese": 90,
    "Salt": 20
}

# Cart to store user-selected items
cart = {}

def display_items():
    print("\nAvailable Grocery Items:")
    print("----------------------------")
    for item, price in grocery_items.items():
        print(f"{item} - ₹{price}")
    print("----------------------------")

def add_to_cart():
    item = input("Enter the item to add: ").capitalize()
    if item in grocery_items:
        qty = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} {item}(s) added to cart.")
    else:
        print("Item not available!")

def remove_from_cart():
    item = input("Enter the item to remove: ").capitalize()
    if item in cart:
        qty = int(input(f"Enter quantity of {item} to remove: "))
        if qty >= cart[item]:
            del cart[item]
            print(f"All {item}(s) removed from cart.")
        else:
            cart[item] -= qty
            print(f"{qty} {item}(s) removed from cart.")
    else:
        print("Item not found in cart!")

def view_cart():
    if not cart:
        print("\nYour cart is empty!")
        return
    print("\nItems in your cart:")
    print("----------------------------")
    total = 0
    for item, qty in cart.items():
        price = grocery_items[item] * qty
        print(f"{item} x {qty} = ₹{price}")
        total += price
    print("----------------------------")
    print(f"Total = ₹{total}")

def checkout():
    if not cart:
        print("Your cart is empty! Add items before checkout.")
        return
    view_cart()
    print("\nThank you for shopping with us! 🛒")
    exit()

# Main menu loop
while True:
    print("\n--- Grocery Store Menu ---")
    print("1. View Items")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        display_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("Exiting the store. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")