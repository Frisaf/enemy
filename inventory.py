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
                return item
            
            else:
                return f"Could not find {item_to_get.name} in your inventory :("

    def add_item(self, item):
        if len(self.contents) < self.size:
            self.contents.append(item)
            
            message = f"Added {item.name} to your inventory."
        
        else:
            message = "Inventory full"
        
        return message

    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)

            message = f"Removed {item.name} from your inventory."
        
        else:
            message = f"{item.name} could not be found in your inventory."
        
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
    def __init__(self):
        self.hotbar = Hotbar(5, "")
        self.inventory = Inventory(10)
    
    def switch_equipped(self, item):
        if item in self.inventory or item in self.hotbar:
            self.hotbar.equipped_item = item

            return "Switched equipped"
        
        else:
            return "Not found"

    def add_to_hotbar(self, item):
        if item in self.inventory.contents:
            self.hotbar.add_item(item)
            self.inventory.remove_item(item)
            
            return "Added", item
        
        else:
            return "Not found", item

def print_inventory_contents():
    for item in inventory.get_contents():
        print(f"{item.name}: {item.description}")

player = Player()
inventory = player.inventory
apple = Consumable("Apple", 0.08, "Crispy!", ["Heal"])
sword = Weapon("Sword", 3, "Slice your enemies down!", 10, 100, ["Soul catcher"])
pumpkin = Consumable("Pumpkin", 5, "Spooky!", ["Heal"])

print(inventory.add_item(apple))
print(inventory.add_item(sword))

# ADD ITEM TO HOTBAR

item_to_add = player.add_to_hotbar(apple)

if item_to_add[0] == "Added":
    print(f"Added {item_to_add[1].name} to inventory.")

else:
    print(f"Could not find {item_to_add[1].name}.")

inventory.contents[0].print_info()

print_inventory_contents()

print(inventory.get_item(apple).description)
print(inventory.get_item(pumpkin))
print(inventory.remove_item(sword))
print(inventory.clear())

inventory.add_item(pumpkin)

print_inventory_contents()