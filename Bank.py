print('Welcome to the Bank module!')
Name=(str(input('Please enter your name: ')))
account_number=(int(input('Please enter your account number: ')))
lis_Ac_number=[1010,2020,3030,4040,5050]         # list of valid account numbers

if account_number in lis_Ac_number:             # Account number validation
    print (f'hello {Name}, your account number {account_number} in valid.')
else:
    print('Invalid account number. Please check and try again.')
    exit()
   
account_balance={1010:5000,2020:3000,3030:7000,4040:6000,5050:8000}             # dictionary of account balances
while True:
    print('1.Check Account Balance \n 2.Deposit Money \n 3.Withdraw Money \n 4.Exit')
    choice= int(input('Please enter your choice: '))

    if choice==1:
        print(f"Your account balance is: {account_balance[account_number]} INR")     # account balance retrieval

    elif choice ==2:
        deposit_amount=int(input('Enter amount to deposit: '))
        account_balance[account_number] += deposit_amount                            # deposit money
        print(f"Amount deposited successfully. New balance is: {account_balance[account_number]} INR")

    elif choice==3:
        withdraw_amount=int(input('Enter amount to withdraw: '))
        if withdraw_amount > account_balance[account_number]:                        # withdraw money with balance check
            print('Insufficient balance.')
        else:
                account_balance[account_number] -= withdraw_amount
                print(f"Amount withdrawn successfully. New balance is: {account_balance[account_number]} INR")   

    elif choice==4:
        print('Thank you for using our banking services. Goodbye!')
        break
    else:
     print(f'Invalid choice. {choice}Please try again.')