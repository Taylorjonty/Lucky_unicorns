def yes_no(question_text):
    while True:

        answer = input(question_text ).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please answer 'yes' or 'no'")


def instructions():
    print("**** How to play *****")
    print()
    print("The rules of the game will go here")
    print()


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


played_before = yes_no("Have you played this game before? ")


if played_before == "No":
    instructions()

user_balance = num_check("how much would you like to play for $ ", 1, 100)
print(f"you are playing with ${user_balance}")
