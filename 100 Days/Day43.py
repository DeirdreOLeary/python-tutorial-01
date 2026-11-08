# Implement encapsulation in a class.

class BankAccount:
    def __init__(self, amount):
        self.__amount = amount
    
    @property
    def deposit(self):
        return self.__amount
    
    @deposit.getter
    def deposit(self):
        return f"You have deposited {self.__amount} to your bank account.\n"
    
    @deposit.setter
    def deposit(self, new_amount):
        if not isinstance(new_amount, int):
            raise TypeError("Deposit amount must be an integer.\n")
        if new_amount > 0:
            self.__amount = new_amount
        else:
            raise ValueError("Deposit amount cannot be a negative value.\n")


# valid deposit amount
d = BankAccount(300)
print(d.deposit)

# invalid deposit amount
d.deposit = -100