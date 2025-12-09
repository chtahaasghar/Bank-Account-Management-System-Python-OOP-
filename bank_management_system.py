import random


class BankAccount:
    def __init__(self,account_number,holder_name,balance,pin):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
        self.__pin = pin
        
    def get_account_number(self):
        return self.__account_number
    
    def get_holder_name(self):
        return self.__holder_name
        
    def get_pin(self):
        return self.__pin
    
    def t_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
        return self.__balance
    def get_balance(self):
        return f"Your Total Balance is:{self.__balance}."
    def get_details(self):
        return f"Account no:{self.__account_number}, Account Name:{self.__holder_name}, Account Balace:{self.__balance}, Pin:{self.__pin}"

all_accounts = []

def find_account_by_pin(pin_input):
    for account in all_accounts:
        # Access the private attribute using the getter method
        if account.get_pin() == pin_input:
            return account
    return None # Return None if no account is found

# Function to find an account by Account Number
def find_account_by_number(acc_no_input):
    for account in all_accounts:
        if account.get_account_number() == acc_no_input:
            return account
    return None

while True:
    print("1:Create new account")
    print("2:Perform Operation")
    print("3:View All Account(Admin)")
    print("4:Exit program")

    select_option = int(input("Select Option:"))
    if select_option == 4:
        print("Exiting Banking System. Goodbye!")
        break

    if select_option == 1:
        acc_no = random.randint(100000,900000)
        name = input("Enter Username:")
        while True:
            balance = float(input("Enter Opening Account Balance (Min 500): "))
            if balance >= 500:
                break
            else:
                print("Opening balance must be at least 500!")
        pin = int(input("Enter 4 Digit Pin:"))
        all_accounts.append(BankAccount(acc_no,name,balance,pin))

    elif select_option == 2:
        d_acc = int(input("Enter Your Account no:"))
        d_account = find_account_by_number(d_acc)
        if d_account:
            d_pin = int(input("Enter Your 4 Digits Pin:"))
            if d_account.get_pin() == d_pin:
                while True:
                    print("1:Deposit money")
                    print("2:Withdraw money")
                    print("3:Check balance")
                    print("4:View account details")
                    print("5:Transfer money between accounts")
                    print("6:Exit program")
                    select_opt = int(input("Select Option:"))
                    if select_opt == 6:
                        print("Exiting Banking System. Goodbye!")
                        break

                    if select_opt == 1:
                        a_deposit = float(input("Enter Deposit Amount:"))
                        if a_deposit>0:
                            new_balance = d_account.deposit(a_deposit)
                            new_balance = d_account.deposit(a_deposit)
                            print(f"Deposited {a_deposit}. New Balance: {new_balance}")
                        else:
                            print("Please Enter Correct Amount!")
                    elif select_opt == 2:
                        a_withdraw = float(input("Enter Withdraw Amount:"))
                        if a_withdraw <= d_account.t_balance():
                            new_balance = d_account.withdraw(a_withdraw)
                        else:
                            print("insufficient Balance")
                    elif select_opt == 3:
                        print(f"Your Balance:{d_account.t_balance()}")
                    elif select_opt == 4:
                        print(d_account.get_details())
                    elif select_opt == 5:
                        d_acc = int(input("Enter Sender Account no:"))
                        receiver_account = find_account_by_number(d_acc)
                        if receiver_account:
                            send_amount = float(input("Enter transfer Amount:"))
                            if send_amount <= d_account.t_balance():
                                d_account.withdraw(send_amount)
                                receiver_account.deposit(send_amount)
                                print(f"{send_amount} PKR is Transfer successfully to {receiver_account.get_account_number()} from {d_account.get_account_number()}.")
                            else:
                                print("insufficient Balance")
                        else:
                            print("❌ Invalid Account. Account not found.")
            else:
                print("❌ Invalid pin. Account not found.")
        else:
            print("❌ Invalid Account. Account not found.")        
    elif select_option == 3:
        admin_pin = 9876
        enter_pin = int(input("Enter Your Security Pin:"))
        if admin_pin == enter_pin:
            if all_accounts:
                print("\n--- All Account Details ---")
                for account in all_accounts:
                    print(account.get_details())
                print("-" * 25)
            else:
                print("No accounts have been created yet.")
        else:
            print("❌ Invalid pin.")