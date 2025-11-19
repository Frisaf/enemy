from inventory import *
from tkinter import *
import random

player = Player(100, 5)
inventory = player.inventory

root = Tk()

root.title("Inventory")
root.geometry("500x600")
heading = Label(root, text = "Inventory program")
inventory_contents_label = Label(text = "YOUR INVENTORY: ")
heading.pack(pady=20)
inventory_contents_label.pack(padx=20)
info_text = Label(root, text = "")

def display_inventory():
    all_items = ""

    for item in inventory.get_contents():
        all_items += f" {item.name},"

    inventory_contents_label.configure(text = f"YOUR INVENTORY: {all_items}")

def random_item():
    item = random.choice(list(items.values()))

    if inventory.add_item(item)[0] == "Added":
        info_text.configure(text = f"Picked up {item.name}")
    
    else:
        info_text.configure(text = "Your inventory is full!")

    info_text.pack()
    display_inventory()

def remove_item():
    item_to_remove = remove_item_entry.get()

    if len(inventory.contents) > 0:
        for item in inventory.contents:
            if item.name == item_to_remove.lower().capitalize():
                inventory.remove_item(item)
                info_text.configure(text = f"Removed {item_to_remove} from your inventory")
                info_text.pack()
                display_inventory()

                return
            
            elif item_to_remove == "":
                info_text.configure(text = "Please provide an item to remove.")

            else:
                info_text.configure(text = f"Could not find {item_to_remove} in inventory.")
    
        display_inventory()
    
    else:
        info_text.configure(text = "Your inventory is empty.")
    
    info_text.pack()

def create_item():
    try:
        name = create_item_name.get()
        type = create_item_type.get().lower().capitalize()
        weight = int(create_item_weight.get())
        description = create_item_description.get()
        ability = create_item_ability.get()
    
    except ValueError:
        info_text.configure(text = "The weight has to be a number.")
        info_text.pack()
    
    if name == "" or type == "" or description == "" or ability == "":
        info_text.configure(text = "Please provide a name, type, description and ability.")
        info_text.pack()

        return
    
    if type == "Consumable":
        new_item = Consumable(name, weight, description, [ability])
    
    elif type == "Weapon":
        try:
            damage = int(create_weapon_damage.get())
            durability = int(create_weapon_durability.get())
        
        except ValueError:
            info_text.configure("The weight and the durability have to be numbers")
            info_text.pack()

        new_item = Weapon(name, weight, description, damage, durability, ability)
    
    else:
        info_text.configure("Your item type has to be either a Weapon or a Consumable")
        info_text.pack()
    
    return new_item

add_item_button = Button(root, text = "Pick up a random item", command = random_item).pack(pady=10)
remove_item_info = Label(text = "Remove an item from your inventory by writing its name in the text box below.").pack(pady=10)
remove_item_entry = Entry(root, width=50)
remove_item_entry.pack()
remove_item_button = Button(root, text = "Remove item", command=remove_item).pack(pady=4)

create_item_name = Entry(root, width=30)
create_item_type = Entry(root, width=30)
create_item_weight = Entry(root, width=20)
create_item_description = Entry(root, width=30)
create_item_ability = Entry(root, width=30)
create_weapon_damage = Entry(root, width=20)
create_weapon_durability = Entry(root, width=20)

create_item_button = Button(root, text = "Create new item", command = create_item)

Label(text = "CREATE A NEW ITEM").pack()
Label(text = "Item name").pack()
create_item_name.pack(pady=4)
Label(text = "Item type (Weapon or Consumable)").pack()
create_item_type.pack(pady=4)
Label(text = "Item weight (Type a number)").pack()
create_item_weight.pack(pady=4)
Label(text = "Item description").pack()
create_item_description.pack()
Label(text = "Item ability").pack()
create_item_ability.pack()
Label(text = "If you want to create a weapon, how much damage does it deal? (Type a number)").pack()
create_weapon_damage.pack()
Label(text = "And how high durability does it have? (Type a number)").pack()
create_weapon_durability.pack()

create_item_button.pack(pady=4)

root.mainloop()