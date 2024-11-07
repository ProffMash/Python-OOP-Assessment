class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute for balance
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def get_balance(self):
        # Public method to get the current balance without modifying it
        return self.__balance

# Demonstrating depositing and withdrawing money
my_account = BankAccount(100)  # Initial balance of 100
print("Initial Balance:", my_account.get_balance())

# Depositing money
my_account.deposit(50)
print("Balance after deposit:", my_account.get_balance())

# Withdrawing money
my_account.withdraw(30)
print("Balance after withdrawal:", my_account.get_balance())


