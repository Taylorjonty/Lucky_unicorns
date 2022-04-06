def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "please enter a number between {} and {}\n".format(low,high)

    while True:
        try:
            respnse = int(input(question))

            if low <= respnse <= high:
                return respnse
            else:
                print(error)

        except ValueError:
            print(error)


user_balance = num_check("how much would you like to play for $ ", 1, 100)
print(f"you are playing with ${user_balance}")
