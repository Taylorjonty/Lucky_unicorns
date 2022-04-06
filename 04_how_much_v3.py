error = "that was not a valid answer \n"
user_balance = 0

while not 1<= user_balance <= 10:
    try:
        user_balance = int(input("please enter a whole number between 1 and 10"
                                 "\n how much would you like to play with $"))
        print()

    except ValueError:
        print(error)

print(f"you are playing with ${user_balance}")
