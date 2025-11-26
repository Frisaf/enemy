from abc import ABC, abstractmethod

class Item:
    def __init__(self, name: str, weight: float, description: str, abilities: list):
        self.name = name
        self.weight = weight
        self.description = description
        self.abilities = abilities

    @abstractmethod
    def use(self):
        pass
    
    def print_info(self) -> str:
        print(self.description)

class Consumable(Item):
    def __init__(self, name: str, weight: float, description: str, abilities: list):
        super().__init__(name, weight, description, abilities)

class Weapon(Item):
    def __init__(self, name: str, weight: float, description: str, abilities: list, damage: int, durability: int):
        super().__init__(name, weight, description, abilities)
        self.damage = damage
        self.durability = durability

class Inventory:
    def __init__(self, size):
        self.contents = []
        self.size = size

    def get_contents(self) -> list:
        return self.contents

    def get_item(self, item_to_get: str) -> Item | str:
        for item in self.contents:
            if item_to_get == item:
                return "Found", item
            
            else:
                return "Not found", item_to_get

    def add_item(self, item):
        if len(self.contents) < self.size:
            self.contents.append(item)
            
            message = "Added", item
        
        else:
            message = "Inventory full", item
        
        return message

    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)

            message = "Removed", item
        
        else:
            message = "Not found", item
        
        return message
    
    def clear(self):
        for item in self.contents:
            self.contents.remove(item)
        
        return "Inventory cleared"

class Hotbar(Inventory):
    def __init__(self, size: int, equipped_item):
        super().__init__(size)
        self.equipped_item = equipped_item

class Player:
    def __init__(self, hp, inventory_size):
        self.hotbar = Hotbar(5, "")
        self.inventory = Inventory(inventory_size)
        self.hp = hp
    
    def switch_equipped(self, item):
        # if item in self.inventory.contents or item in self.hotbar.contents:
        #     self.hotbar.equipped_item = item

        #     return "Switched equipped"
        
        # else:
        #     return "Not found"

        for thing in self.inventory.contents:
            if item == thing.name:
                self.hotbar.equipped_item = thing

                return "Switched equipped"
        
        for thing in self.hotbar.contents:
            if item == thing.name:
                self.hotbar.equipped_item = thing

                return "Switched equipped"
        
        return "Not found"

    def add_to_hotbar(self, item):
        # if item in self.inventory.contents:
        #     self.hotbar.add_item(item)
        #     self.inventory.remove_item(item)
            
        #     return "Added", item
        
        # else:
        #     return "Not found", item

        for thing in self.inventory.contents:
            if item == thing.name:
                self.hotbar.add_item(thing)
                self.inventory.remove_item(thing)
            
                return "Added", thing
            
            else:
                return "Not found", thing
    
    def get_equipped(self):
        equipped_item = self.hotbar.equipped_item

        return equipped_item.name

def print_inventory_contents():
    for item in inventory.get_contents():
        print("YOUR INVENTORY")
        print(f"{item.name}: {item.description}")

def print_add_inventory(function):
    if function[0] == "Added":
        print(f"Added {function[1].name} to inventory")
    
    else:
        print(f"Could not find {function[1].name}")

def print_add_hotbar(function):
    if function[0] == "Added":
        print(f"Added {function[1].name} to hotbar.")
    
    else:
        print(f"Could not find {function[1].name}.")

def print_get_item(function):
    if function[0] == "Not found":
        print(f"Could not find {function[1].name}")
    
    else:
        print(function[1].name)

def print_remove_inventory(function):
    if function[0] == "Removed":
        print(f"Removed {function[1].name} from inventory.")
    
    else:
        print(f"Could not find {function[1].name}.")

player = Player(100, 5)
inventory = player.inventory

items = {
    "Apple": Consumable("Apple", 0.08, "Crispy!", ["Heal"]),
    "Sword": Weapon("Sword", 3, "Slice your enemies down!", 10, 100, ["Soul catcher"]),
    "Pumpkin": Consumable("Pumpkin", 5, "Spooky!", ["Heal"])
}

### TEST CODE I MADE TO SEE IF IT WORKED ###

# apple = items["Apple"]
# sword = items["Sword"]
# pumpkin = items["Sword"]

# print_add_inventory(inventory.add_item(apple))
# print_add_inventory(inventory.add_item(sword))

# # ADD ITEM TO HOTBAR
# print_add_hotbar(player.add_to_hotbar(apple))

# inventory.contents[0].print_info()

# print_inventory_contents()

# print_get_item(inventory.get_item(apple))
# print_get_item(inventory.get_item(pumpkin))

# print_remove_inventory(inventory.remove_item(sword))

# print(inventory.clear())

# inventory.add_item(pumpkin)

# print_inventory_contents()

# player.switch_equipped(apple)
# print(f"Current equipped item: {player.get_equipped()}")