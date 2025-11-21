from inventory import *
from tkinter import *
import random

player = Player(100, 5)
inventory = player.inventory

root = Tk()

root.title("Inventory")
root.geometry("500x860")
inventory_contents_label = Label(text = "YOUR INVENTORY:")
inventory_contents = Text(height = 6, width = 50)
equipped_item = Label(text = "EQUIPPED ITEM: ")

inventory_contents_label.pack(padx=20)
inventory_contents.pack()
equipped_item.pack()

info_text = Label(root, text = "")
info_text.pack()

def display_inventory():
    all_items = ""

    for item in inventory.get_contents():
        all_items += f" {item.name} - {item.description}\n"
    
    inventory_contents.delete("1.0", END)
    inventory_contents.insert(END, all_items)

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
                
                remove_item_entry.delete(0, END)

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
        weight = float(create_item_weight.get())
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
    
    inventory.add_item(new_item)
    display_inventory()
    info_text.configure(text = f"{new_item.name} has been created and added to your inventory.")

    create_item_name.delete(0, END)
    create_item_type.delete(0, END)
    create_item_description.delete(0, END)
    create_item_ability.delete(0, END)
    create_item_weight.delete(0, END)

    create_weapon_damage.delete(0, END)
    create_weapon_durability.delete(0, END)

def equip_item():
    item_to_equip = equip_item_entry.get().lower().capitalize()

    if item_to_equip != "":
        equip = player.switch_equipped(item_to_equip)

        if equip != "Switched equipped":
            info_text.configure(text = f"Equipped {item_to_equip}")
            equipped_item.configure(text = f"EQUIPPED ITEM: {item_to_equip}")
        
        else:
            info_text.configure(text = f"Couldn't find {item_to_equip}")
    
    else:
        info_text.configure(text = "Please provide an item to equip")

def hotbar():
    item_to_add = add_item_hotbar.get().lower().capitalize()

    if item_to_add != "":
        hotbar = player.add_to_hotbar(item_to_add)

        if hotbar[0] != "Added":
            info_text.configure(text = f"Added {item_to_add} to hotbar")
        
        else:
            info_text.configure(text = f"Couldn't find {item_to_add}")
    
    else:
        info_text.configure(text = "Please provide an item to add to hotbar.")
            

add_item_button = Button(root, text = "Pick up a random item", command = random_item).pack(pady=10)
remove_item_info = Label(text = "Remove an item from your inventory by writing its name in the text box below.").pack(pady=10)
remove_item_entry = Entry(root, width=50)
remove_item_entry.pack()
remove_item_button = Button(root, text = "Remove item", command=remove_item).pack(pady=4)

equip_item_entry = Entry(root, width=50)
Label(text = "Equip an item from your inventory/hotbar").pack()
equip_item_entry.pack()
equip_item_btn = Button(root, text = "Equipp item", command = equip_item).pack(pady=4)

add_item_hotbar = Entry(root, width = 50)
Label(text = "Add an item to your hotbar").pack()
add_item_hotbar.pack()
add_item_hotbar_btn = Button(root, text = "Add item to hotbar", command = hotbar).pack(pady=4)

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
Label(text = "Item weight in kg (Type a number)").pack()
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