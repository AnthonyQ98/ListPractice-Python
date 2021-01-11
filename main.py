
passwordOld = ["ItIsPassword", "NumberTwo", "Test"]
usernameOld = ["Test", 'Anthony98', 'Testing']


def username():
    while True:
        print("Enter your username: ")
        username = input()
        if username in usernameOld:
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
        if password in passwordOld:
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

username()
password()


mainOrder = ['Big Mac Meal', 'McChicken Sandwich Meal', 'Nuggets']
sideOrder = ['Fries', 'Fruit bag', 'Curly Fries']
desert = ['McFlurry', 'Cookie', 'McMuffin', 'Donut']

menu_menu = [['Big Mac Meal', 12.50], ['McChicken Sandwich Meal', 10.50], ['Nuggets', 7.50],
             ['Fries', 3.30], ['Fruit bag', 1.50], ['Curly Fries', 4.50],
             ['McFlurry', 3.50], ['Cookie', 2.20], ['McMuffin', 2.00], ['Donut', 2.50]]


def drivethru():
    global menu, total, counter, quantityList
    menu = []
    quantityList = []
    total = 0
    counter = 0
    print("*" * 50, "\n Main: ", ", ".join(mainOrder), "\n Side: ", ", ".join(sideOrder),
          "\n Desert: ", ", ".join(desert))
    while True:
        print("Please choose what you'd like or press 2 to checkout: ")
        pick = input()
        for sublist in menu_menu:
            if pick == sublist[0]:
                print("Quantity: ")
                quantity = int(input())
                quantityList.append(quantity)
                if quantity < 1:
                    print("Error, please enter a quantity of 1 or more.")
                    quantity = int(input())
                total += sublist[1] * quantity
                menu.append(pick)
                if quantity == 1:
                    print(str(pick) + " added to your order.")
                else:
                    print(str(quantity), str(pick) + "'s" " added to your order.")
            elif pick == '2':
                for item_a, item_b in zip(menu, quantityList):
                    counter += 1
                    print("Item {2}: {0:20} Quantity: {1}".format(item_a, item_b, counter))
                print("Your total is: €" + str(round(total, 2)))

                return total, menu

def checkout():
    while True:
        print("*" * 20, "Checkout Page", "*" * 20)
        full_name = input("Full Name: ")
        addressLine1 = input("Address Line 1: ")
        addressLine2 = input("Address Line 2: ")
        addressline3 = input("Address Line 3: ")
        city = input("City/Town: ")
        phone_number = input("Phone Number: ")
        email = input("Email Address: ")
        while full_name == '' or addressLine1 == '' or phone_number == '' or email == '':
            if full_name == '':
                full_name = input("Enter a full Name: ")
            elif addressLine1 == '':
                addressLine1 = input("Enter a address: ")
            elif phone_number == '':
                phone_number = input("Enter a phone Number: ")
            elif email == '':
                email = input("Enter a email Address: ")
        print("Press 1 to submit your details or 2 to cancel.")
        verify = input()
        if verify == '1':
            print("Thank you for submitting your order. Your order will be processed soon.")
            break
        else:
            continue


drivethru()
checkout()

counter = 0
for item_a, item_b in zip(menu, quantityList):
    counter += 1
    print("Item {2}: {0:20} Quantity: {1}".format(item_a, item_b, counter))
print("Your total bill for your order above is €" + str(total))
print("Thank you for ordering!")

print("End of program.")

