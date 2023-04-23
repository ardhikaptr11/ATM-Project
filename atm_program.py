import random
import datetime
from customer import Customer

print('Ardhika Finance, Ltd.')
print('====================')

# Instantiate Customer class
atm = Customer(id)

# Empty dict to store the account number and account name
transfer_data = {}


# This is to store User's PIN
# Changeable if the User changes the PIN through the menu (old -> new)
user_info = {
    'cust_pin': atm.checkPin()
}

# This is to track User's deposit transaction per day
# If the User exceeds the daily limit, the transaction fails
total_transaction = 0
transaction_info = {
    'min_save': atm.MIN_SAVE,
    'max_save': atm.MAX_SAVE,
    'total': total_transaction
}


def withdraw_yes():
    atm.withdrawBalance(nominal_input)
    print('\nThe transaction is successful!')
    print(f'Recent balance: Rp {atm.checkBalance():,}')


def deposit_yes():
    atm.depositBalance(nominal_input)
    print('\nThe transaction is successful!')
    print(f'Recent balance: Rp {atm.checkBalance():,}')


# Function to look up matches in the transfer_data dictionary
# The function will return all the matches account name and account number
def search(keyword):
    matches = []
    for key, value in transfer_data.items():
        if keyword.lower() in value.lower():
            matches.append((key, value))
    if len(matches) == 0:
        return
    if len(matches) == 1:  # At least only one user found
        print('\nA user found!')
        print('')
    else:
        print(f'\n{len(matches)} users found!')  # More than one user found
        print('')
    for i, match in enumerate(matches):
        print(f'{i+1}. {match[1]} - {match[0]}')
    while True:
        select_input = int(input('\nSelect your transfer destination (just the number): '))  # Users are prompted to select a transaction destination
        if 1 <= select_input <= len(matches):  # If User pressed a number within the range of the returned name list, the transaction continues
            break
        else:
            print('\nHINT: Select the only number that exist')
    return matches[select_input-1]


# User are prompted to enter PIN
while True:

    id_ = input('Enter PIN: ')
    while len(id_) != 6:   # Check if PIN has length of 6 digits
        print('\nHINT: PIN consists of 6 digit numbers\n')
        id_ = input('Re-enter PIN: ')

    trial = 1
    while id_ != user_info['cust_pin']:  # PIN has 6 digits but entered PIN is invalid
        print('\nInvalid PIN...\n')
        id_ = input('Re-enter PIN: ')
        while len(id_) != 6:
            id_ = input('Re-enter PIN: ')
        trial += 1
        if trial == 3:
            print('\nYou\'ve entered the wrong PIN many times')
            print('Yor account blocked for a while')
            print('If this considered as a mistake\nContact us via Customer Service (1-700555)')
            exit()

    while True:  # If PIN is valid and consists of 6 digits, User can access services
        print('\nWelcome to  Ardhika Finance, Ltd.\n')
        print('Please select menu:\n 1 - Balance Check \n 2 - Debit \n 3 - Deposit \n 4 - Change PIN \n 5 - Transfer \n 6 - Exit ')

        selectmenu = int(input('Enter here: '))

        if selectmenu == 1:  # Balance check menu
            print(f'\nYour total balance: Rp {atm.checkBalance():,}')

        if selectmenu == 2:  # Debit menu
            print('\n1. Prioritize Rp 50,000\n2. Prioritize Rp 100,000\n3. Cancel')
            user_input = int(input('Please enter: '))

            if user_input == 1:  # If users want to prioritize Rp. 50.000
                nominal_input = int(input('\nEnter nominal: '))  # Users can enter minimum of Rp 50.000 and its multiples
                MIN_NOMINAL_50 = 50_000
                # Check if User entered a valid nominal
                # If User's total balance is sufficient to make a transaction
                if nominal_input % MIN_NOMINAL_50 == 0 and nominal_input >= atm.checkBalance():
                    print('\nInsufficient balance,')
                    print('Please top up your balance.')
                elif nominal_input % MIN_NOMINAL_50 == 0 and nominal_input < atm.checkBalance():
                    print(f'The amount of Rp {nominal_input:,} will be deducted from your balance. \nAre you sure?')
                    print('1. Yes\n2. No')
                    user_confirm = int(input('Please enter (just the number): '))
                    if user_confirm == 1:
                        input_pin = input('Enter PIN: ')
                        if input_pin == user_info['cust_pin']:
                            withdraw_yes()
                        else:
                            print('PIN invalid')
                            break
                    elif user_confirm == 2:
                        print('Cancelling...')
                        print('Directing to main menu...')
                # Entered nominal is invalid
                while nominal_input % MIN_NOMINAL_50 != 0:
                    print('\nPlease enter valid nominal of Rp 50.000')
                    nominal_input = int(input('Enter nominal: '))  # This will attempt User to enter valid nominal
                    # If entered nominal is valid but will result zero balance, the transaction fails
                    if nominal_input % MIN_NOMINAL_50 == 0 or nominal_input >= atm.checkBalance():
                        print('\nInsufficient balance,')
                        print('Please top up your balance.')
                    elif nominal_input % MIN_NOMINAL_50 == 0 and nominal_input < atm.checkBalance():
                        print(f'The amount of Rp {nominal_input:,} will be deducted from your balance. \nAre you sure?')
                        print('1. Yes\n2. No')
                    user_confirm = int(input('Please enter (just the number): '))
                    if user_confirm == 1:
                        input_pin = input('Enter PIN: ')
                        if input_pin == user_info['cust_pin']:
                            withdraw_yes()
                        else:
                            print('PIN invalid')
                            break
                    elif user_confirm == 2:
                        print('Cancelling...')
                        print('Directing to main menu...')

            if user_input == 2:  # If users want to prioritize Rp. 100.000
                nominal_input = int(input('\nEnter nominal: '))  # User can enter minimum of Rp 100.000 and its multiples
                MIN_NOMINAL_100 = 100_000
                # Check if User's total balance is sufficient to make a transaction
                # Fail when the total balance is insufficient
                if nominal_input % MIN_NOMINAL_100 == 0 and nominal_input >= atm.checkBalance():
                    print('\nInsufficient balance,')
                    print('Please top up your balance.')
                elif nominal_input % MIN_NOMINAL_100 == 0 and nominal_input < atm.checkBalance():
                    print(f'The amount of Rp {nominal_input:,} will be deducted from your balance. \nAre you sure?')
                    print('1. Yes\n2. No')
                    user_confirm = int(input('Please enter (just the number): '))
                    if user_confirm == 1:
                        input_pin = input('Enter PIN: ')
                        if input_pin == user_info['cust_pin']:
                            withdraw_yes()
                        else:
                            print('PIN invalid')
                            break
                    elif user_confirm == 2:
                        print('Cancelling...')
                        print('Directing to main menu...')
                # Entered nominal is invalid
                while nominal_input % MIN_NOMINAL_100 != 0:
                    print('\nPlease enter valid nominal of Rp 100.000')
                    nominal_input = int(input('Enter nominal: '))  # This will attempt User to enter valid nominal
                    # If entered nominal is valid but will result zero balance, the transaction fails
                    if nominal_input % MIN_NOMINAL_100 == 0 or nominal_input >= atm.checkBalance():
                        print('\nInsufficient balance,')
                        print('Please top up your balance.')
                    # Entered nominal is valid and the total balance is sufficient
                    elif nominal_input % MIN_NOMINAL_100 == 0 and nominal_input < atm.checkBalance():
                        print(f'The amount of Rp {nominal_input:,} will be deducted from your balance. \nAre you sure?')
                        print('1. Yes\n2. No')
                        user_confirm = int(input('Please enter (just the number): '))
                        if user_confirm == 1:
                            input_pin = input('Enter PIN: ')
                            if input_pin == user_info['cust_pin']:
                                withdraw_yes()
                            else:
                                print('PIN invalid')
                                break
                        elif user_confirm == 2:
                            print('Cancelling...')
                            print('Directing to main menu...')

            # User chooses to cancel
            if user_input == 3:
                print('Directing to main menu...')

        elif selectmenu == 3:  # Deposit menu
            while True:
                print('\nNOTE: Rp 10.000 is the minimum deposit')
                print('HINT: Type \'0\' to cancel\n')
                nominal_input = int(input('Enter nominal: '))  # Users are prompted to enter a nominal
                if nominal_input == 0:
                    break
                # Entered nominal satisfies the minimum transaction
                if nominal_input < transaction_info['min_save']:
                    continue
                # The total transaction has exceeded the daily limit, next attempt the transaction fails
                if total_transaction + nominal_input > transaction_info['max_save']:
                    print('Transaction failed!')
                    print('HINT: You have reached the daily limit')
                    break

                # The transaction nominal entered by the User will be calculated
                total_transaction += nominal_input
                # User confirmation if nominal entered satisfies the minimum transaction
                print(f'The amount of Rp {nominal_input:,} will be added to your balance. \nAre you sure?')
                print('1. Yes\n2. No')
                user_confirm = int(input('Please enter (just the number): '))
                if user_confirm == 1:
                    deposit_yes()
                elif user_confirm == 2:
                    print('Cancelling...')
                    print('Directing to main menu...')

        if selectmenu == 4:  # Change PIN menu
            print('\nAre you sure want to change PIN?')
            print('1. Yes\n2. No')
            user_input = int(input('Please enter (just the number): '))

            if user_input == 1:
                old_pin = input('\nEnter your old PIN: ')
                if old_pin == user_info['cust_pin'] and old_pin.isdigit():  # To check if entered PIN is valid
                    print('\nJust a second...')
                    new_pin = input('\nEnter a new 6-digit PIN: ')
                    while len(new_pin) != 6 or (not new_pin.isdigit()):  # If the User tries to enter an invalid format
                        print('\nMake sure you enter a valid format')
                        new_pin = input('Enter a new 6-digit PIN: ')
                    if new_pin != user_info['cust_pin'] and new_pin.isdigit():  # The new PIN should not be the same as the old PIN that is already stored
                        verify_new_pin = input('Re-enter new PIN: ')  # Users are prompted to re-enter new PIN to confirm
                        while verify_new_pin != new_pin:  # Re-entered PIN has not matched the previously entered PIN
                            print('\nYou entered different PIN')
                            verify_new_pin = input('Re-enter new PIN: ')
                        if verify_new_pin == new_pin:
                            print('\nWe have successfully changed your PIN!\n')
                            print('Please re-enter PIN to continue')
                            user_info.update({'cust_pin': new_pin})  # The old PIN is replaced by a new PIN
                            break
                    else:  # If the User tries to enter the old PIN as the new one
                        while new_pin == old_pin:
                            print('\nHINT: Cannot enter your old PIN')
                            new_pin = input('Enter a new 6-digit PIN: ')
                        while not new_pin.isdigit():
                            print('\nMake sure you enter a valid format')
                            new_pin = input('Enter a new 6-digit PIN: ')
                        verify_new_pin = input('Re-enter new PIN: ')
                        while new_pin != verify_new_pin or (not verify_new_pin.isdigit()):
                            print('\nYou entered different PIN')
                            verify_new_pin = input('Re-enter new PIN: ')
                        if verify_new_pin == new_pin:
                            print('\nWe have successfully changed your PIN!\n')
                            print('Please re-enter PIN to continue')
                            user_info.update({'cust_pin': new_pin})
                            break
                else:  # On the first try the user entered the PIN incorrectly, the system will cancel the transaction
                    print('\nInvalid PIN')
                    print('Transaction cancelled...')
            elif user_input == 2:  # The user chooses to cancel the transaction
                print('Cancelling...')
                print('Directing to main menu...')

        elif selectmenu == 5:  # Transfer menu
            while True:
                print('\n 1. Register account number\n 2. List of registered account numbers\n 3. Transfer\n 4. Cancel')
                user_input = int(input('Please enter (just the number): '))

                if user_input == 1:  # This menu is used to register an account before the user can make a transfer
                    print('\nWARNING: You can\'t go back if you have a typo.')
                    print('So make sure you input the right number.')
                    print('\nHINT: press \'0\' to cancel')
                    acc_num = input('Enter 10-digits account number: ')  # User are asked to enter a valid account number
                    if acc_num == '0':  # Press 0 to cancel
                        break
                    while len(acc_num) != 10 or (not acc_num.isdigit()):  # On the First try, User enters an invalid format
                        print('\nMake sure the account number consists of 10 digits of number')
                        acc_num = input('\nEnter 10-digits account number: ')
                    if acc_num not in transfer_data:  # If account number entered by User is not found in transfer_data dict
                        name_input = input('Enter the name of the account owner: ')
                        while len(name_input) < 3 or name_input.isdigit():  # Name at least has 3 characters long
                            print("\nHINT: Name must be at least 3 characters long and can't be a number")
                            name_input = input('Enter the name of the account owner: ')
                        transfer_data[acc_num] = name_input.title()
                        print('\nAccount number has successfully registered!')
                    else:
                        print('\nEntered account number has already registered.')  # If an account already exists in transfer_data dict

                elif user_input == 2:  # User can see all the account that has already registered
                    index_no = 1
                    print("\nList of registered account number:")
                    sorted_transfer_data = dict(sorted(transfer_data.items(), key=lambda x: x[1]))  # This is to sort account list alphabetically (A-Z)
                    for number, name in sorted_transfer_data.items():
                        print(f"{index_no}. {name.title()} - {number}")
                        index_no += 1

                elif user_input == 3:
                    print('\nHINT: press \'0\' to cancel')
                    input_keyword = input('Enter the account owner\'s : ')
                    matched_user = search(input_keyword)
                    if input_keyword == '0':  # Press 0 to cancel
                        break
                    if matched_user:  # The keyword or name entered by the User matches the data in the transfer_data dict
                        account_number = matched_user[0]
                        name = matched_user[1]
                        nominal_input = int(input('Enter nominal: '))
                        if nominal_input >= atm.checkBalance():  # Insufficient balance, the transaction fails
                            print('\nInsufficient balance,')
                            print('Please top up your balance.')
                            print('\nTransaction cancelled...')
                        else:  # If the User has sufficient balance, transaction details will be displayed
                            print('')
                            print('TRANSACTION DETAIL'.center(30, '-'))
                            confirm_message = f"Account No\t: {account_number}\nOwner name\t: {name}\nNominal\t\t: Rp {nominal_input:,}"
                            print(confirm_message)
                            user_confirm = input('\nPress (Y)es to continue or (N)o to cancel: ')
                            if user_confirm == 'y':
                                withdraw_yes()
                            elif user_confirm == 'n':
                                print('\nCancelling...')
                                print('Directing to main menu...')
                                break
                    else:
                        print(f'\nNo match to the user with the name \'{input_keyword}\'')  # Keyword or name has no match

                elif user_input == 4:  # The User chooses to cancel
                    break

        elif selectmenu == 6:
            print('\nReceipt will be printed automatically\nPlease keep this receipt as proof of your transaction.\n')
            print(f'Record No\t\t: {random.randint(10000, 1000000)}')
            print(f'Transaction date\t: {datetime.datetime.now()}')
            print(f'Final balance\t\t: Rp {atm.checkBalance():,}')
            print('\nThank you for using our services!')
            print('Ardhika Finance, Ltd., HiTech Tower 233rd Floor, IKN Town - Indonesia')
            print('Customer Care (1-700555)')
            exit()
