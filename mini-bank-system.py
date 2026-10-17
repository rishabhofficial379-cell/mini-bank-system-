
import time

print("================================")
print("      WELCOME TO OUR BANK")
print("================================")

accounts = {
    "rahul": 1000,
    "priya": 2000,
    "ankit": 1500
}

pin = {
    "rahul": 1234,
    "priya": 5678,
    "ankit": 9012
}

wrong_attempts = 0
lock_time = 30 * 60

name = input("Please enter your name: ").lower()

if name in accounts:
    print("Welcome,", name)

    while wrong_attempts < 3:
        entered_pin = input("Please enter your PIN: ")

        if entered_pin.isdigit() and int(entered_pin) == pin[name]:
            print("PIN verified successfully!")
            print("Access granted.")
            break

        else:
            wrong_attempts = wrong_attempts + 1
            print("Incorrect PIN!")
            print("Attempts left:", 3 - wrong_attempts)

    if wrong_attempts == 3:
        print("Too many incorrect attempts!")
        print("Your access is locked for 30 minutes.")

        time.sleep(lock_time)

        print("Lock finished. Please run the program again.")

    else:
        while True:
            print()
            print("========== BANK MENU ==========")
            print("1. Check balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Change PIN")
            print("5. Exit")
            print("===============================")

            choice = input("Choose an option: ")

            if choice == "1":
                print("Your current balance is: Rs.", accounts[name])

                if accounts[name] == 0:
                    print("No money left in your account!")

            elif choice == "2":
                deposit_amount = input("Enter deposit amount: ")

                if deposit_amount.isdigit():
                    deposit_amount = float(deposit_amount)

                    if deposit_amount > 0:
                        accounts[name] = accounts[name] + deposit_amount
                        print("Deposit successful!")
                        print("Your new balance is: Rs.", accounts[name])

                    else:
                        print("Please enter a valid amount.")

                else:
                    print("Please enter numbers only.")

            elif choice == "3":
                if accounts[name] == 0:
                    print("No money left in your account!")

                else:
                    withdraw_amount = input("Enter withdrawal amount: ")

                    if withdraw_amount.isdigit():
                        withdraw_amount = float(withdraw_amount)

                        if withdraw_amount <= 0:
                            print("Please enter a valid amount.")

                        elif withdraw_amount > accounts[name]:
                            print("Insufficient balance!")
                            print("Your current balance is: Rs.", accounts[name])

                        else:
                            accounts[name] = accounts[name] - withdraw_amount
                            print("Withdrawal successful!")
                            print("Your remaining balance is: Rs.", accounts[name])

                            if accounts[name] == 0:
                                print("No money left in your account!")

                    else:
                        print("Please enter numbers only.")

            elif choice == "4":
                old_pin = input("Enter your current PIN: ")

                if old_pin.isdigit() and int(old_pin) == pin[name]:
                    new_pin = input("Enter your new 4-digit PIN: ")

                    if new_pin.isdigit() and len(new_pin) == 4:
                        pin[name] = int(new_pin)
                        print("PIN changed successfully!")

                    else:
                        print("PIN must contain exactly 4 digits.")

                else:
                    print("Incorrect current PIN!")

            elif choice == "5":
                print("Thank you for using our bank,", name)
                break

            else:
                print("Invalid choice! Please select 1 to 5.")

else:
    print("Account not found!")
