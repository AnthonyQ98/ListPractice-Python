passwordOld = ["ItIsPassword", "NumberTwo", "Test"]
usernameOld = ["Pauline98", 'Anthony98', 'Testing']


def username():
    while True:
        print("Enter your username: ")
        username = input()
        if username == usernameOld[2]:
            print("Correct Username!")
            break
        else:
            print("Incorrect Username!")
            continue


def password():
    passwordattempts = 0
    while True:
        print("Enter your password: ")
        password = input()
        if password == passwordOld[1]:
            print("Successful login!")
            break
        else:
            passwordattempts += 1
            passwordtry = 5 - passwordattempts
            print("Password incorrect, you have " + str(passwordtry) + " attempts left.")
            if passwordattempts == 5:
                print("You have ran out of attempts, please try again in five minutes.")
            else:
                continue

# username()
# password()


mainOrder = ['Big Mac Meal', 'McChicken Sandwich Meal', 'Nuggets']
sideOrder = ['Fries', 'Fruit bag', 'Curly fries']
desert = ['McFlurry', 'Cookie', 'McMuffin', 'Donut']

menu_menu = [['Big Mac Meal', 12.50], ['McChicken Sandwich Meal', 10.50], ['Nuggets', 7.50],
             ['Fries', 3.30], ['Fruit bag', 1.50], ['Curly fries', 4.50],
             ['McFlurry', 3.50], ['Cookie', 2.20], ['McMuffin', 2.00], ['Donut', 2.50]]


def drivethru():
    menu = []
    total = 0
    print("*" * 50, "\n Main: ", mainOrder, "\n Side: ", sideOrder, "\n Desert: ", desert)
    while True:
        print("Please choose what you'd like or press 2 to checkout: ")
        pick = input()
        for sublist in menu_menu:
            if pick == sublist[0]:
                total += sublist[1]
                menu.append(pick)
                print(str(pick) + " added to your order.")
            elif pick == '2':
                print("Your order: \n", ", ".join(menu))
                print("Your total is: €" + str(round(total, 2)))
                return total, menu


drivethru()

print("Hello!")

