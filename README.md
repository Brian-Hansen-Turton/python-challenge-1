# UPENN-VIRT-AI-PT-07-2024-U-LOLC - Module 2 Challenge

## Project Overview

This project is a Python-based console application designed to simulate a food truck ordering system. The program presents a menu to the customer, allows them to select items from various categories, and calculates the total cost of the selected items. The goal of this project is to practice working with dictionaries, loops, and conditional statements in Python.

## How to Use

1. **Run the Program:** Start the application by running the Python script.
2. **Select Menu Category:** The program will display the main menu categories. Select the category from which you want to order by typing the corresponding number.
3. **Select Items:** Once a category is selected, the program will display the items in that category with their prices. Choose the item you want by typing the corresponding number.
4. **Specify Quantity:** After selecting an item, you will be prompted to enter the quantity. If the input is invalid, the program defaults to a quantity of 1.
5. **Continue or Complete Order:** After selecting an item, you can choose to continue ordering or finalize your order.
6. **View Order Summary:** Once the order is completed, the program will display a summary of all ordered items and the total cost.

## Example Output

```plaintext
Welcome to the variety food truck.
From which menu would you like to order? 
1: Snacks
2: Meals
3: Drinks
4: Dessert
Type menu number: 2
You selected Meals.
What Meals item would you like to order?
Item # | Item name                 | Price
-------|---------------------------|-------
1      | Burrito                   | $4.49
2      | Teriyaki Chicken          | $9.99
3      | Sushi                     | $7.49
4      | Pad Thai                  | $6.99
5      | Pizza - Cheese            | $8.99
6      | Pizza - Pepperoni         | $10.99
7      | Pizza - Vegetarian        | $9.99
8      | Burger - Chicken          | $7.49
9      | Burger - Beef             | $8.49
Please Enter the number of the item you would like to order 2
How many Teriyaki Chicken would you like to order? The default is 1. 2
Would you like to keep ordering? (Y)es or (N)o N
Thank you for your order

This is what we are preparing for you.

Item name                  | Price  | Quantity
---------------------------|--------|----------
Teriyaki Chicken           | $9.99  | 2

The total cost of all times is $19.98
