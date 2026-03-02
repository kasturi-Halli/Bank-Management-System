from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass

class Bank(Account):
    
    def deposit(self, amount):
        print("Deposited:", amount)

    def withdraw(self, amount):
        print("Withdrawn:", amount)

b = Bank()
b.deposit(1000)
b.withdraw(500)

class SavingsAccount:
    def withdraw(self, balance, amt):
        if balance - amt >= 500:
            print("Savings Withdraw Success")
            return balance - amt
        print("Minimum balance required")
        return balance

class CurrentAccount:
    def withdraw(self, balance, amt):
        if amt <= balance + 1000:
            print("Current Withdraw Success")
            return balance - amt
        print("Overdraft limit exceeded")
        return balance


# Demo
balance = 1000

sa = SavingsAccount()
balance = sa.withdraw(balance, 300)

ca = CurrentAccount()
balance = ca.withdraw(balance, 200)

print("Final Balance:", balance)