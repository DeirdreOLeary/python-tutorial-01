# Create a class for a bank account with methods for deposit and withdrawal.

class BankAccount:
    def __init__(self, amount):
        self.amount = amount
    
    def deposit(self):
        print(f"You have deposited {self.amount} to your bank account.")
    
    def withdrawal(self):
        print(f"You have withdrawn {self.amount} from your bank account.")


# deposit
d = BankAccount(300)
d.deposit()

# withdrawal
w = BankAccount(5000)
w.withdrawal()