# Program to demonstrate encapsulation and abstraction

from abc import ABC, abstractmethod


# Abstract class
class Bank(ABC):

    # Abstract method
    @abstractmethod
    def calculate_interest(self):
        pass


# Child class
class Account(Bank):

    def __init__(self, name, balance):
        self.name = name

        # Private variable - Encapsulation
        self.__balance = balance

    # Method to display balance
    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

    # Implementation of abstract method
    def calculate_interest(self):
        interest = self.__balance * 0.05
        print("Interest:", interest)


# Creating object
account = Account("Anant", 10000)

# Calling methods
account.display_balance()
account.calculate_interest()