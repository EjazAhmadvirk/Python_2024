# ----------------------------------------
# OOP Principles in Python
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction
# ----------------------------------------

from abc import ABC, abstractmethod  # For abstraction

# --------------------------
# 1. Abstraction
# --------------------------
# Creating an abstract class using ABC
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Encapsulated attribute

    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (must be implemented by subclasses)

# --------------------------
# 2. Inheritance + 3. Polymorphism
# --------------------------
# Dog class inherits from Animal and implements the abstract method
class Dog(Animal):
    def make_sound(self):  # Polymorphism: different behavior for same method
        return "Woof!"

# Cat class also inherits from Animal and implements the abstract method
class Cat(Animal):
    def make_sound(self):  # Polymorphism
        return "Meow!"

# --------------------------
# 4. Encapsulation
# --------------------------
# Using private attributes with getter and setter
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (encapsulated)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Modifying private attribute
            print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Getter method
        return self.__balance

# --------------------------
# Main logic to test everything
# --------------------------
# Testing Inheritance + Polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")  # Runtime Polymorphism

print()

# Testing Encapsulation
account = BankAccount("Ejaz", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Final balance: {account.get_balance()}")

# Trying to access private variable directly (will fail)
# print(account.__balance)  # Uncommenting this will raise an error
