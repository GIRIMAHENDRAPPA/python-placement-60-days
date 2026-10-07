import json
import os

# --- Custom Exceptions ---
class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

DATA_FILE = "data.json"

# --- Load / Save File ---
def load_data():
    try:
        if not os.path.exists(DATA_FILE):
            return {}
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"File Error: {e}, Starting fresh database")
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Failed to save file: {e}")

# --- Bank Logic ---
class Bank:
    def __init__(self):
        self.accounts = load_data()

    def create_account(self, acc_no, name, balance=0):
        try:
            if acc_no in self.accounts:
                raise ValueError("Account already exists!")
            if balance < 0:
                raise InvalidAmountError("Opening balance cannot be negative")
            
            self.accounts[acc_no] = {"name": name, "balance": balance}
            save_data(self.accounts)
            print(f"Account {acc_no} created for {name}")
        except Exception as e:
            print(f"Error: {e}")

    def deposit(self, acc_no, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Deposit amount must be > 0")
            if acc_no not in self.accounts:
                raise ValueError("Account not found")
            
            self.accounts[acc_no]["balance"] += amount
            save_data(self.accounts)
            print(f"Deposited {amount}. New Balance: {self.accounts[acc_no]['balance']}")
        except (InvalidAmountError, ValueError) as e:
            print(f"Transaction Failed: {e}")

    def withdraw(self, acc_no, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Withdraw amount must be > 0")
            if acc_no not in self.accounts:
                raise ValueError("Account not found")
            if self.accounts[acc_no]["balance"] < amount:
                raise InsufficientBalanceError(f"Only {self.accounts[acc_no]['balance']} available, tried {amount}")

            self.accounts[acc_no]["balance"] -= amount
            save_data(self.accounts)
            print(f"Withdrew {amount}. New Balance: {self.accounts[acc_no]['balance']}")
        except (InvalidAmountError, InsufficientBalanceError, ValueError) as e:
            print(f"Transaction Failed: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            print("--- Transaction Attempt Complete ---")

    def show(self):
        if not self.accounts:
            print("No accounts")
            return
        for acc_no, info in self.accounts.items():
            print(f"{acc_no} | {info['name']} | Rs. {info['balance']}")

# --- Main Menu ---
if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1.Create 2.Deposit 3.Withdraw 4.Show All 5.Exit")
        choice = input("Choose: ")
        try:
            if choice == "1":
                acc = input("Acc No: ")
                name = input("Name: ")
                bal = int(input("Opening Balance: "))
                bank.create_account(acc, name, bal)
            elif choice == "2":
                acc = input("Acc No: ")
                amt = int(input("Amount: "))
                bank.deposit(acc, amt)
            elif choice == "3":
                acc = input("Acc No: ")
                amt = int(input("Amount: "))
                bank.withdraw(acc, amt)
            elif choice == "4":
                bank.show()
            elif choice == "5":
                print("Saved to data.json. Bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter numbers only for amount!")