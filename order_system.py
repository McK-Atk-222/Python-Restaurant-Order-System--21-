def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order_list = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    continue_ordering = True
    # A continuous while loop so customers can order multiple items
    while continue_ordering:
        # Asks the customer what they want to order
        print("What would you like to order? ")

        # Create a variable for the menu item number
        i = 1

        # Print the menu header
        print_menu_heading()

        # Loops through the menu dictionary
        # Extracts the food category and the options for each category
        for food_category, options in menu.items():

            # Loops through the options for each food category
            # Extracts the meal and the price for each option
            for meal, price in options.items():

                # Print the menu item number, food category, meal, and price
                print_menu_line(i, food_category, meal, price)

                # Update the menu selection number
                i += 1

        # Asks customer to input menu item number
        menu_selection = input("Type menu number: ")

        # Updates the order list using the update_order function
        # Sends the order list, menu selection, and menu items as arguments
        order_list=update_order(order_list, menu_selection, menu_items)

        # Asks the customer if they would like to order anything else
        # Lets the customer know if they should type 'n' or 'N' to quit
        continue_ordering = input("Would you like to keep ordering? (N) to quit: ")

        # A conditional statement that checks the user's input
        # The conditional statement checks for 'n' or 'N'
        if continue_ordering.lower() == "n":

            # A print statement that thanks the customer for their order
            print ("Thank you for your order.")


            # Uses list comprehension to create a list called prices_list,
            # which contains the total prices for each item in the order list:
            # The total price for each item should multiply the price by quantity
            price_list = [item["Quantity"] * item["Price"] for item in order_list]

            # Creates an order_total from the prices list using sum()
            # Rounds the prices to 2 decimal places.
            order_total = round(sum(price_list),2)

            # Exits the ordering loop
            continue_ordering = False 

    # Returns the order list and the order total
    return order_list, order_total

def update_order(order_list, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # Checks if the customer typed a number
    if menu_selection.isdigit():
        # Converts the menu selection to an integer
        menu_selection = int(menu_selection)

        # Checks if the menu selection is in the menu items keys
        if menu_selection in menu_items.keys():
            # Stores the item name as a variable
            item_name = menu_items[menu_selection]["Item name"]

            # Asks the customer for the quantity of the menu item
            # Uses the item name variable in the question
            quantity = input(f"What quantity of {item_name} would you like? \n"
                             + "(This will default to 1 if number is not entered)\n")

            # Checks if the quantity is a number, default to 1 if not
            if not quantity.isdigit():
                quantity = 1
            else: 
                quantity=int(quantity)
            # Adds a dictionary to the order list 
            # The dictionary includes the item name, price, and quantity
            # Used the following names for the dictionary keys:
            # "Item name", "Price", "Quantity"
            order_list.append({
                "Item name" : menu_items[menu_selection]["Item name"],
                "Price" : menu_items[menu_selection]["Price"],
                "Quantity" : quantity
            })


        # When the user's input isn't valid, 
        # tells the customer that their input isn't valid
        else:
            print ("Sorry, that number isn't an option. \n")

    # When the menu selection wasn't valid:
    # Prints the menu selection and 
    # Tells the customer they didn't select a menu option
            print (f"{menu_selection}, \n" +
            "A menu option hasn't been selected")
    else:
        print (f"{menu_selection} was not a menu option.")
    # Returns the updated order
    return order_list

def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)
    # Loops through the items in the customer's receipt
    for items in receipt:
        # Stores the dictionary items as variables
        item_name=items["Item name"]
        price=items["Price"]
        quantity=items["Quantity"]

        # Prints the receipt line using the print_receipt_line function
        # Sends the item name, price, and quantity as separate arguments
        print_receipt_line(item_name, price, quantity)

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

