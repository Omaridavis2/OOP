import random

class Character:
    def __init__(self, name, health=100, power=100):
        # Public attribute: name
        self.name = name
        # Protected attribute: health
        self._health = health
        # Protected attribute: power
        self._power = power

    def take_damage(self, damage):
        # Public method modifying a class attribute
        self._health -= damage
        print(f"{self.name} took {damage} damage. Current health: {self._health}")

    def use_power(self, cost):
        # Public method modifying a class attribute
        self._power -= cost
        print(f"{self.name} used their power. Current power: {self._power}")


class Superpower:
    def __init__(self, name):
        # Public attribute: name
        self.name = name

    def activate_power(self):
        # Public method using class attributes
        print(f"{self.name} power activated!")


class Superhero(Character):
    def __init__(self, name, health=150, power=150):
        # Inheriting from the Character class
        super().__init__(name, health, power)
        # Composition: Superhero has a Superpower
        self.superpower = Superpower("Flight")

    def fly(self):
        # Public method using class attributes
        self.superpower.activate_power()
        print(f"{self.name} is flying!")


class Villain(Character):
    def __init__(self, name, health=120, power=120):
        # Inheriting from the Character class
        super().__init__(name, health, power)
        # Composition: Villain has a Superpower
        self.superpower = Superpower("Flight")

    def fly(self):
        # Public method using class attributes
        self.superpower.activate_power()
        print(f"{self.name} is flying!")

    def use_power(self, cost):
        # Overriding the use_power method of the superclass
        # Protected method of the superclass called within the subclass
        super().use_power(cost // 2)
        print(f"{self.name} used their enhanced flight speed!")


# Instantiate objects
spartan = Superhero("Spartan")
z_man = Villain("Z-man")

# Test the game
spartan.fly()
z_man.fly()

spartan.take_damage(30)
spartan.use_power(20)

z_man.take_damage(25)
z_man.use_power(15)
