from abc import ABC, abstractmethod

class Item:
    def __init__(self, name: str, weight: float, description: str, type):
        self.name = name
        self.weight = weight
        self.description = description
        self.type = type

    @abstractmethod
    def use(self):
        pass
    
    def print_info(self):
        print(self.description)

class Consumable:
    def __init__(self, abilities: list):
        self.abilities = abilities

class Weapon:
    def __init__(self, damage: int, durability: int, abilities: list):
        self.damage = damage
        self.durability = durability
        self.abilities = abilities

class Inventory:
    def __init__(self, size):
        self.contents = []
        self.size = size

    def get_contents(self):
        return self.contents

    def get_item(self, item_to_get: str) -> Item | None:
        for item in self.contents:
            if item_to_get == item:
                return item.description
            
            elif self.contents[i].name == None:
                return f"Could not find {item.name} in your inventory :("

    def add_item(self, item):
        if len(self.contents) < self.size:
            self.contents.append(item)
            
            message = f"Added {item.name} to your inventory."
        
        else:
            message = "Inventory full"
        
        return message

    @abstractmethod
    def remove_item(self, Item):
        pass

inventory = Inventory(10)
apple = Item("Apple", 0.08, "Crispy!", Consumable(["Heal"]))
sword = Item("Sword", 3, "Slice your enemies down!", Weapon(10, 100, ["Soul catcher"]))
pumpkin = Item("Pumpkin", 5, "Spooky!", Consumable(["Heal"]))

print(inventory.add_item(apple))
print(inventory.add_item(sword))

inventory.contents[0].print_info()

for item in inventory.get_contents():
    print(item.name)

print(inventory.get_item(pumpkin))