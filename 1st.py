import random
import string


def generate_account_number():
    return "".join(random.choices(string.digits, k=10))


class BankAccount:
    def __init__(self, name, opening_balance=0):
        self.account_number = generate_account_number()
        self.name = name
        self.balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def display(self):
        print(f"\nAccount holder: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance:       ${self.balance:.2f}")


def main():
    name = input("Enter account holder name: ").strip()
    account = BankAccount(name)
    print(f"Account created successfully. Number: {account.account_number}")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View account\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "4":
            print("Thank you for banking with us.")
            break
        if choice == "3":
            account.display()
            continue
        if choice in ("1", "2"):
            try:
                amount = float(input("Enter amount: "))
                if choice == "1":
                    account.deposit(amount)
                    print("Deposit successful.")
                else:
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                print(f"Current balance: ${account.balance:.2f}")
            except ValueError as error:
                print(f"Transaction failed: {error}")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()