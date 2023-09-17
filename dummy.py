import random

menu = {
    "Rice": 30,
    "Tea": 10,
    "Chicken Curry": 50,
    "Salad": 20,
    "Pizza": 40
}

orders = {}

def generate_order_id():
    return random.randint(10000, 99999)

# Function to create a new order
def create_new_order():
    order_id = generate_order_id()
    order_items = {}

    print("Menu:")
    for item, price in menu.items():
        print(f"{item} - ${price}")

    while True:
        item = input("Enter the item to add to the order (or 'done' to finish): ")
        if item == 'done':
            break
        elif item in menu:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                order_items[item] = quantity
            else:
                print("Quantity should be greater than 0.")
        else:
            print("Invalid item. Please choose a valid item from the menu.")

    orders[order_id] = order_items
    print(f"Order {order_id} created successfully!")

# Function to view orders and calculate the bill
def view_orders():
    for order_id, order_items in orders.items():
        print(f"Order ID: {order_id}")
        total_cost = 0
        for item, quantity in order_items.items():
            item_price = menu[item]
            item_total = item_price * quantity
            print(f"{item} - Quantity: {quantity} - Price: ${item_total}")
            total_cost += item_total
        print(f"Total Cost: ${total_cost}\n")

# Main menu loop
while True:
    print("\nMain Menu:")
    print("1. Create New Order")
    print("2. View Orders")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_new_order()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Thank you for using The Enchanted Fork restaurant management application!")
