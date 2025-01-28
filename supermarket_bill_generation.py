'''
Write a Python program to generate a bill for a supermarket purchase. T
program should store the items and their prices in a list of tuples. It should
then iterate over this list to print out each item along with its price. Finally,
calculate and print the total cost of all the items

'''



item_list = {
    "rice": 50,
    "flour": 40,
    "sugar": 45,
    "milk": 60,
    "eggs": 70,
    "potatoes": 25,
    "tomotoes": 30,
    "onion": 35,
    "oil": 150,
    "tea": 100

}

total_cost = 0
quantity = 0
cart = {}
while True:
    print("\n1. View Items\n2. Add to Cart\n3. View Cart and Checkout\n4. Exit")
    choice = input("Choose your the option: ").strip()
    if choice == "1":
        print("\nCheckout the items available!")
        print("\nItem      Price")
        print("-"*30)
        for item,price in item_list.items():
            print(f"{item:10}-Rs.{price}")
    
    elif choice == "2":
        while True:
            choice_2 = input("Enter 1 to buy or 2 to go to home page: ").strip()
            if choice_2 == "1":
                item = input("Enter the item name to add to cart:").lower().strip()
                if item in item_list:
                    quantity = int(input("Enter the quantity: "))
                    if item in cart:
                        cart[item] += quantity
                    else:
                        cart[item] = quantity
                else:
                    print("Item not available")
            else:
                print("Back to home page")
                break

    elif choice == "3":
        if not cart:
            print("Your cart is empty")
        else:
            print("\nItem    Quantity    Price")
            print("-"*30)
            for item, quantity in cart.items():
                price = item_list[item] * quantity
                print(f"{item:10} {quantity}    -Rs.{price}")
                total_cost += price
            print("-"*30)
            print(f"Total:          Rs.{total_cost}")

    elif choice == "4":
        print("\nThank you for Shopping! Visit Again!!\n")
        break
    else:
        print("Invalid choice. Please choose a valid option")






    








