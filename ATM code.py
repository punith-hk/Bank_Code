print("Welcome to PM Bank")
restart = ('y')
chances = 3
Balance = 51000
while chances >=0:
    pin = int(input("Please enter your pin: "))
    if pin == (1234):
        print("you entered your pin correctly\n")
        while restart not in ('n', 'N', 'NO', 'no'):
            print("press 1 for your balance\n")
            print("press 2 for withdrawl\n")
            print("press 3 for deposit\n")
            print("press 4 for return card\n")
            option = int(input("what would you like to choose? "))
            if option == 1:
                print("your account balance is Rs.",Balance, '\n')
                restart = input("would you like to go back\n")
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('please enter the amount? \n100,500,2000: '))
                if withdrawl <= Balance:
                    balance = Balance - withdrawl
                    print ("your account balance is",balance,)
                    restart = input('would you like to go back? ')
                    if restart in ('n', 'N', 'NO', 'no'):
                        print("Thank you")
                        break
                elif withdrawl > Balance:
                    print("Insuffient Balance\n")
                    break
            elif option == 3:
                deposit = float(input("Please enter the amount you want to deposit\n"))
                Deposit = deposit + Balance
                print("your account balance is now" ,Deposit)
                restart = input('would you like to go back? ')
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank you")
                    break
            elif option ==4:
                print("Please wait")
                print("Thank you, visit again")
                break
            else:
                print("\nPlease select correct option\n")
                restart = ('y')
    elif pin != 1234:
        chances = chances - 1
        if chances ==1:
            print("Warning: Last Chance, if pin incorrect your card will blocked for 24hours")
        if chances ==0:
            print("\nsorry, you exceed the limin, try after 24 hours\n")
            break