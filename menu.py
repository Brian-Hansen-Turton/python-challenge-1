import utility

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Clear the console - make it look nice ;-) 
utility.clear_console()

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# order_list keys
name_key =  utility.order_item_name_key
price_key = utility.order_item_price_key
quanity_key = utility.order_item_quanity_key

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}.")
            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            name_key: key + " - " + key2,
                            price_key: value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        name_key: key,
                        price_key: value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            item_order_selection = input(f"Please Enter the number of the item you would like to order ")
            
            # 3. Check if the customer typed a number
            if item_order_selection.isdigit():
                # Convert the menu selection to an integer
                item_order_number = int(item_order_selection)

                # 4. Check if the menu selection is in the menu items
                if item_order_number in menu_items:
                    # Store the item name as a variable
                    item_name = menu[menu_category_name]
                    # Ask the customer for the quantity of the menu item
                    quanity = input(f'How many {menu_items[item_order_number][name_key]} would you like to order? The default is 1. ')
                    # Check if the quantity is a number, default to 1 if not
                    if quanity.isdigit():
                        quanity = max(int(quanity), 1) 
                        # Utility 
                        order_list = utility.add_or_update_item(
                            order_list,
                            menu_items[item_order_number][name_key],
                            menu_items[item_order_number][price_key],
                            quanity)
                    
                    # Tell the customer that their input isn't valid
                    else:
                        print(f"Not a valid item {quanity}")
                # Tell the customer they didn't select a menu option
            else:
                print(f"{item_order_selection} is not a valid selection")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")


    while True:
        # Ask the customer if they would like to order anything else
        order_more = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match order_more.lower():
            case 'y':
                # Keep ordering
                place_order = True
                utility.clear_console()
                break

            case 'n':
                # Exit the keep ordering question loop
                place_order = False
                utility.clear_console()
                print("Thank you for your order")  
                break

            case _:
                 print(f"Sorry, {order_more} was an invalid selection please try again.")

            # Tell the customer to try again

# Print out the customer's order
utility.clear_console()
print("\nThis is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order in order_list:
    # 7. Store the dictionary items as variables
    item_name = order[name_key]
    item_price = order[price_key]
    item_quanity = order[quanity_key]
    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${item_price}  | {item_quanity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
all_item_cost = [(item[price_key] * order[quanity_key]) for item in order_list]
total_cost = sum(all_item_cost)
print(f"\nThe total cost of all times is ${total_cost:.2f}\n")