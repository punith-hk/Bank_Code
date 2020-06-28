restart = 'y'
print("Welcome to PM Bank")
print("Please select any options")
while restart not in ['n', 'N']:
    print("Press 1 for Withdrawl")
    print("Press 2 for Deposit")
    print("Press 3 for complients")
    option = int(input("what would you like to choose? "))
    if option == 1:
        print("Please collect your tocken")
        print("Your counter is 'A'")
        break
    if option == 2:
        print("Please collect your tocken")
        print("Your counter is 'B'")
        break
    if option == 3:
        print("Please collect your tocken")
        print("Your counter is 'C'")
        break
    else:
        print("Please select correct option")
        restart = ('y')


print("Thank You")

