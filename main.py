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
    passwordAttempts = 0
    while True:
        print("Enter your password: ")
        password = input()
        if password == passwordOld[1]:
            print("Successful login!")
            break
        else:
            passwordAttempts += 1
            passwordTry = 5 - passwordAttempts
            print("Password incorret, you have " + str(passwordTry) + " attempts left.")
            if passwordAttempts == 5:
                print("You have ran out of attempts, please try again in five minutes.")
            else:
                continue

#username()
#password()

mainOrder = ['Big Mac Meal', 'McChicken Sandwich Meal', 'Nuggets']
sideOrder = ['Fries', 'Fruit bag', 'Curly fries']
desert = ['McFlurry', ]

def drivethru():
    print("*" * 50)

drivethru()

