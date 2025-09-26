class Enemy:
    def __init__(self, health: int, attack: int, name: str): # Constructor
        self.health = health
        self.attack = attack
        self.name = name
    
    def print_status(self):
        print(f"Enemy {self.name}. Health: {self.health}")
    
    def enemy_attack(self):
        print(f"{self.name} farts you in the face (loudly!). It deals {self.attack} damage >:3")
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

jöns = Enemy(10, 10, "Jöns")
jöns.print_status()
jöns.enemy_attack()
jöns.take_damage(10)