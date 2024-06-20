from CardHolder import CardHolder


def print_menu():
    print("\nPlease choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")


def deposit(card_holder):
    try:
        amount = float(input("How much $$ would you like to deposit: "))
        card_holder.set_balance(card_holder.get_balance() + amount)
        print("Thank you. Your new balance is: $", str(card_holder.get_balance()))
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def withdraw(card_holder):
    try:
        amount = float(input("How much $$ would you like to withdraw: "))
        if amount > card_holder.get_balance():
            print("Insufficient funds!")
        else:
            card_holder.set_balance(card_holder.get_balance() - amount)
            print("Thank you. Your new balance is: $", str(card_holder.get_balance()))
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def check_balance(card_holder):
    print("Your current balance is: $", card_holder.get_balance())


def authenticate(card_holders):
    card_number = input("Please enter your card number: ")
    pin = input("Please enter your PIN: ")

    for card_holder in card_holders:
        if card_holder.card_number == card_number and card_holder.check_pin(pin):
            return card_holder
    return None


if __name__ == "__main__":
    # Sample data
    list_of_card_holders = [
        CardHolder("123456789", "1234", "John", "Doe", 100.0),
        CardHolder("987654321", "5678", "Jane", "Doe", 200.0)
    ]

    authenticated_user = authenticate(list_of_card_holders)

    if authenticated_user:
        print(f"Welcome {authenticated_user.first_name} {authenticated_user.last_name}!")

        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                deposit(authenticated_user)
            elif choice == '2':
                withdraw(authenticated_user)
            elif choice == '3':
                check_balance(authenticated_user)
            elif choice == '4':
                print("Thank you for using our ATM service. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a valid option.")
    else:
        print("Authentication failed! Please check your card number and PIN.")
