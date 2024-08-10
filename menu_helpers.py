import os
import platform

def clear_console():
    # Check if the operating system is Windows
    if platform.system() == "Windows":
        os.system("cls")
    else:
        # If not Windows, assume it's a Unix-like system (Linux, macOS, etc.)
        os.system("clear")

order_item_name_key = "Item name"
order_item_price_key = "Price"
order_item_quanity_key = "Quanity" 

def add_to_order(list, name, price, quanity):

    if len(list) == 0:
        list.append({order_item_name_key: name,
                     order_item_price_key: price,
                     order_item_quanity_key: quanity}) 

    for index, item in enumerate(list):
        if item[order_item_name_key] == name:
            print("all ready in list")
            new_quanity = quanity * item[order_item_quanity_key]
            list[index] = ({order_item_name_key: name,
                 order_item_price_key: price,
                 order_item_quanity_key: new_quanity})
            print(f"{list}")
        else:
            list.append({order_item_name_key: name,
                        order_item_price_key: price,
                        order_item_quanity_key: quanity})  
    print(f"{list}")
    return list    
