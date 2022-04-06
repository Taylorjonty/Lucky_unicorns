error = "please enter a whole number between 1 and 10\n"
valid = False

while not valid:
    try:
        user_balance = injt(input("How much would you like to play with $"))

        if 0 < user_balance <= 10:
            print(f"you are playing with {user_balance}")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)

user_balance = int(input("How much do you want to play with(must be a "
                         "interger between 1 and 10"

while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10")

    user_balance = int(input("how much do you want to play with $"))

print(f"you are playing with ${user_balance}")
