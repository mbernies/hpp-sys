def menu():
    print("Choose from the options below:")
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3")
    print("[0] Option 0")
def option1():
    print("\nYou choose option 1!")
def option2():
    print("\nYou choose option 2!")
def option3():
    print("\nYou choose option 3!")
def option0():
    print("\nGoodbye!")
menu()
option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    else:
        print("\nInvalid option!")
    print()
    menu()
    option = int(input("Enter your option: "))
option0()
