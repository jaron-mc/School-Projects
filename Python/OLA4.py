# Jaron McCutcheon
# CSCI 1170-D01
# ola4
# This program simulates a bank account application

def main():
    print("d - Deposit\tw - Withdrawal\tr - Repeating payments\tq - Quit")
    selection = input("Please choose from one of the above options: ")
    print("")

    if selection == 'd':
        d()
    elif selection == 'w':
        w()
    elif selection == 'r':
        r()
    elif selection == 'q':
        q()
    else:
        print("Error: Invalid menu option. Please select from one of the above menu options.")
        main()


def d():
    global balance
    while True:
        deposit = float(input("Deposit amount must be positive. Enter the deposit amount: "))
        if deposit > 0:
            balance = balance + deposit
            print(f"You deposited ${deposit:,.2f}. Your new balance is ${balance:,.2f}")
            main()
            break


def w():
    global balance
    while True:
        withdrawal = float(input("Enter the withdrawal amount: "))
        if withdrawal < 1:
            print("Withdrawal amount must be positive. ", end="")
        elif withdrawal > balance:
            print("You do not have sufficient funds. Withdrawal denied!")
            main()
            break
        else:
            balance -= withdrawal
            print(f"You withdrew ${withdrawal:,.2f}. Your new balance is ${balance:,.2f}")
            main()
            break


def r():
    global balance
    while True:
        payment_amount = float(input("Please enter the payment amount: "))
        payment_n = int(input("Please enter the number of payments: "))
        if payment_amount < 0 or payment_n < 0:
            print("Error: Payment amount and number of payments must be positive.")
        elif payment_amount * payment_n > balance:
            print("You do not have sufficient funds to cover requested payments. Payments denied!")
            main()
            break
        else:
            for i in range(payment_n):
                i += 1
                balance -= payment_amount
                print(f"Payment {i} for ${payment_amount:,.2f} is made. Your new balance is ${balance:,.2f}.")
            main()
            break


def q():
    print(f"Final balance: ${balance:,.2f}")
    print("Have a good day.")


balance = float(input("Enter the starting balance: "))
print(f"You have a balance of ${balance:,.2f}")
main()
