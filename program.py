import time, random

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

class Enemy:
    def __init__(self, health: int, attack: int, name: str, x, y): # Constructor
        self.health = health
        self.attack = attack
        self.name = name
        self.alive = True
        self.x = x
        self.y = y
    
    def print_status(self):
        print(f"Enemy {self.name}. Health: {self.health}. Position: ({self.x}, {self.y})")
    
    def take_damage(self, damage):
        if self.is_alive() == True:
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
    
    def check_collision(self, target): # Check if two characters' positions are the same
        if self.x == target.x and self.y == target.y:
            return True # They collide
        
        else:
            return False # They don't collide

    def move(self, dir):
        direction = dir.lower()
        if direction == "up":
            if self.y == 3:
                print(f"{self.name} are at the upper edge of the board. They move further up.")
            
            else:
                self.y += 1
        
        elif direction == "down":
            if self.y == 0:
                print(f"{self.name} are at the lower edge of the board. They can't move further down.")
            
            else:
                self.y -= 1
            
        elif direction == "right":
            if self.x == 3:
                print(f"{self.name} are at the right edge of the board. They can't move further right.")
            
            else:
                self.x += 1
        
        elif direction == "left":
            if self.x == 0:
                print(f"{self.name} are at the left edge of the map. They can't move further left.")
            
            else:
                self.x -= 1

jöns_attack = int(20 / random.randint(1, 5))
petrus_attack = int(20 / random.randint(1, 5))

jöns_x = 0
jöns_y = 0

petrus_x = 3
petrus_y = 3

jöns = Enemy(100, jöns_attack, "Jöns", jöns_x, jöns_y)
petrus = Enemy(100, petrus_attack, "Petrus", petrus_x, petrus_y)

directions = ["up", "down", "right", "left"]

while jöns.is_alive() == True and petrus.is_alive() == True:
    jöns.print_status()
    petrus.print_status()

    jöns.enemy_attack(petrus)
    petrus.enemy_attack(jöns)

    if jöns.check_collision(petrus) != True:
        jöns.move(random.choice(directions))
        petrus.move(random.choice(directions))

    time.sleep(1)
    print("")