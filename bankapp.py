import sys
import getpass

bank = {
    'user': ['ram', 'hari', 'john'],
    'acc': [1001, 1002, 1003],
    'password': ['redhat', 'python', 'java'],
    'bal': [10000, 20000, 1000000]
}

def openAccount():
    global bank

    print("\n\nWelcome to Open Account Service - ")

    user_name = input("\n\nEnter User Name - ")
    user_password = getpass.getpass("\n\nEnter your password - ")
    user_bal = int(input("\n\nEnter How much mony you want to deposit into account - "))

    user_acc = bank['acc'][-1] + 1

    print("\n\nWe are processing your information \n\n")

    bank['user'].append(user_name)
    bank['acc'].append(user_acc)
    bank['bal'].append(user_bal)
    bank['password'].append(user_password)

    print("A new Account is sucessfully created ")
    print("\n Please Write down your information and don't share it with anyone \n\n")

    print("Name = ", user_name)
    print("Acc NO. = ", user_acc)
    print("Account Balance = ", user_bal)
    print("Your Password = ", user_password)

    print("\n\n Welcome To my bank service \n\n")

    menu()

def loginAccount():
    global bank
    user_name = input("\n\nEnter User Name - ")
    user_password =input("\n\nEnter your password - ")
    count = user_password++

while count <= 2
    if user_password = bank['password']:
         print('password is authenticated you are logged in')
    else:
         print("Wrong password try again, \n you have 2 more tries :")


def deleteAccount():
    global bank
    print('To delete an account you need to login first')
    loginAccount()
    check = input('Are you sure you want to delete this account, y/n')
    if check = 'y':
     del bank ['user'], bank ['acc'], bank ['password'], bank ['bal']
    else:
     print("\n\n Welcome To my bank service \n\n")

    menu()

def menu():
    print("Welcome to any bank services - \n\n\n")
    print("Please Choose Your Option - ")
    print("1.Open a new Account")
    print("2.Login into your Account")
    print("3.Delete Account")
    print("4.Exit")

    op = int(input("\n\n\t\tEnter your option :- "))

    if op == 1:

        openAccount()


    elif op == 2:

        loginAccount()


    elif op == 3:

        deleteAccount()

    else:

        sys.exit(1)

