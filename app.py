from inventory import *
from tkinter import *
import random

player = Player(100, 5)
inventory = player.inventory

root = Tk()

root.title("Inventory")
root.geometry("500x500")
heading = Label(root, text = "Inventory program")
heading.pack()
info_text = Label(root, text = "")

def display_inventory():
    all_items = ""

    for item in inventory.get_contents():
        all_items += f" {item.name},"

    heading.configure(text = f"YOUR INVENTORY: {all_items}")

def random_item():
    item = random.choice(list(items.values()))

    if inventory.add_item(item)[0] == "Added":
        info_text.configure(text = f"Picked up {item.name}")
    
    else:
        info_text.configure(text = "Your inventory is full!")

    info_text.pack()

def remove_item():
    item_to_remove = remove_item_entry.get()

    for item in inventory.contents:
        if item.name == item_to_remove.lower().capitalize():
            inventory.remove_item(item)
            info_text.configure(text = f"Removed {item_to_remove} from your inventory")

        else:
            info_text.configure(text = f"Could not find {item_to_remove} in inventory.")

inventory_button = Button(root, text = "Display Inventory Contents", command=display_inventory).pack()
add_item_button = Button(root, text = "Pick up a random item", command = random_item).pack()
remove_item_info = Label(text = "Remove an item in the text box by writing its name").pack()
remove_item_entry = Entry(root, width=50)
remove_item_entry.pack()
remove_item_button = Button(root, text = "Remove item", command=remove_item).pack()

root.mainloop()