import time, random

class Enemy:
    def __init__(self, health: int, attack: int, name: str): # Constructor
        self.health = health
        self.attack = attack
        self.name = name
    
    def print_status(self):
        print(f"Enemy {self.name}. Health: {self.health}")
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")
    
    def enemy_attack(self, target):
        print(f"{self.name} farts {target.name} in the face (loudly!). They deal {self.attack} damage >:3")
        target.take_damage(self.attack)
    
    def is_alive(self):
        if self.health <= 0:
            print(f"{self.name} is dead!")
            return False
        
        else:
            print(f"{self.name} is still alive and has {self.health} HP left.")
            return True

jöns_attack = int(20 / random.randint(1, 5))
petrus_attack = int(20 / random.randint(1, 5))

jöns = Enemy(100, jöns_attack, "Jöns")
petrus = Enemy(100, petrus_attack, "Petrus")

while jöns.is_alive() == True and petrus.is_alive() == True:
    jöns.enemy_attack(petrus)
    petrus.enemy_attack(jöns)
    time.sleep(1)
    print("")