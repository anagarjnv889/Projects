class BankAccount:
    def __init__(self, acc_holder_name, balance=0):
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Account Holder name: {self.acc_holder_name}")
        print(f"Current balance: ₹{self.balance}")

def show_menu():
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    print("Welcome to the Python Bank!")
    acc_holder_name = input("Enter your name to create an account: ")
    account = BankAccount(acc_holder_name)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
