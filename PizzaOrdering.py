class Pizza:
    def __init__(self, name, size, crust, toppings):
        self.name = name
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.price = self.calculate_price()

    def calculate_price(self):
        base_price = 10  # Base price for pizza
        size_price = {"small": 2, "medium": 4, "large": 6}  # Additional price based on size
        crust_price = {"thin": 1, "thick": 2, "stuffed": 3}  # Additional price based on crust
        topping_price = len(self.toppings) * 1.5  # Additional price per topping

        total_price = base_price + size_price[self.size.lower()] + crust_price[self.crust.lower()] + topping_price
        return total_price

    def __str__(self):
        return f"{self.size.capitalize()} {self.crust.capitalize()} {self.name} Pizza"

def order_pizza():
    print("Welcome to Pizza Delight!")
    print("Please select the type of pizza you'd like to order:")
    print("0. Exit")
    print("1. Margherita")
    print("2. Pepperoni")
    print("3. Veggie")
    print("4. Hawaiian")
    print("5. Custom Pizza")

    while True:
        choice = input("Enter your choice (0-5): ")
        if choice == "0":
            print("Thank you for visiting Pizza Delight. Goodbye!")
            return
        elif choice == "1":
            pizza_type = "Margherita"
            break
        elif choice == "2":
            pizza_type = "Pepperoni"
            break
        elif choice == "3":
            pizza_type = "Veggie"
            break
        elif choice == "4":
            pizza_type = "Hawaiian"
            break
        elif choice == "5":
            pizza_type = "Custom"
            break
        else:
            print("Invalid choice. Please try again.")

    print(f"\nYou have selected: {pizza_type}.")

    size = input("What size would you like? (Small, Medium, Large): ")
    while size.lower() not in ["small", "medium", "large"]:
        print("Invalid size. Please try again.")
        size = input("What size would you like? (Small, Medium, Large): ")
    print(f"\nYou have selected: {size.capitalize()}.")

    crust = input("What type of crust would you like? (Thin, Thick, Stuffed): ")
    while crust.lower() not in ["thin", "thick", "stuffed"]:
        print("Invalid crust. Please try again.")
        crust = input("What type of crust would you like? (Thin, Thick, Stuffed): ")
    print(f"\nYou have selected: {crust.capitalize()} crust.")

    if pizza_type == "Custom":
        toppings = input("Enter the toppings for your custom pizza (separated by commas): ").split(",")
    else:
        toppings = []

    pizza = Pizza(pizza_type, size, crust, toppings)
    print("\nOrder Summary:")
    print(pizza)
    print(f"Total Price: ${pizza.price}")

    confirm = input("\nWould you like to place the order? (Y/N): ")
    if confirm.upper() == "Y":
        print("Your pizza order has been placed. Thank you for visiting Pizza Delight!")
    else:
        print("Order cancelled. But hey, thank you for visiting Pizza Delight!")

order_pizza()