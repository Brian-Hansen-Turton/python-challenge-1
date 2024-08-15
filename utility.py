import os
import platform

def clear_console():
    """ This function will clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

order_item_name_key = "Item name"
order_item_price_key = "Price"
order_item_quanity_key = "Quanity" 

# add new items to the list, or upate quanity if 
# item is already in the list
def add_or_update_item(list, name, price, quanity):
    new_item = {order_item_name_key: name,
                order_item_price_key: price,
                order_item_quanity_key: quanity}
    """This helper function will add a new order, or update the quanity if already ordered. """
    
    for item in list:
        if item[order_item_name_key] == new_item[order_item_name_key]:
            item[order_item_quanity_key] += new_item[order_item_quanity_key]
            break
    else:
        list.append(new_item)
        
    return list    