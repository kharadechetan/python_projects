class FoodDelivery:
    def __init__(self):
        self.menu = {
            "Pizza": 10.99,
            "Burger": 5.99,
            "Pasta": 8.99,
            "Salad": 4.99,
            "Sushi": 12.99
        }
        self.cart = {}

    def display_menu(self):
        print("\n=== Menu ===")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def add_to_cart(self, item, quantity):
        if item in self.menu:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
            print(f"Added {quantity}x {item} to cart.")
        else:
            print("Item not found in menu.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\n=== Your Cart ===")
        total = 0
        for item, quantity in self.cart.items():
            price = self.menu[item] * quantity
            total += price
            print(f"{item} x{quantity} - ${price:.2f}")
        print(f"Total: ${total:.2f}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add items before checkout.")
            return
        self.view_cart()
        print("Order placed successfully! 🎉")
        self.cart.clear()

def food_delivery_system():
    system = FoodDelivery()
    while True:
        print("\n=== Food Delivery System ===")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_menu()
        elif choice == "2":
            item = input("Enter the food item: ").title()
            quantity = int(input("Enter quantity: "))
            system.add_to_cart(item, quantity)
        elif choice == "3":
            system.view_cart()
        elif choice == "4":
            system.checkout()
        elif choice == "5":
            print("Thank you for using the Food Delivery System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    food_delivery_system()
