import random


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
    print()
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


def generate_token(balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1  # to keep track of rounds
        number = random.randint(1, 100
    )  # can only be a donkey

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (adds $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("$", "Congratulations, you go a unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("!", "Oh no, you got a donkey"))
            print()

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.5 from balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5
                print(formatter("#", "Darn, you go a zebra"))
                print()
            # if the number is odd, set the token to horse
            else:
                token = "horse"
                balance -= 0.5
                print(formatter("#", "Darn, you go a horse"))
                print()

        print(f"Round {rounds_played}. Token {token}, Balance: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               "again or 'X' to exit ").lower()

        print()
    return balance


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the lucky unicorn game"))
print()
played_before = yes_no("Have you played this game before? ")


if played_before == "No":
    instructions()

starting_balance = num_check("how much would you like to play for $ ", 1, 100)
print(f"you are playing with ${starting_balance}")
print()

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print(formatter("*", "Goodbye"))
