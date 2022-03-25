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
    print("program continues")
    print()
played_before = yes_no("Have you played this game before? ")
if played_before == "No":
    instructions()
else:
    print("program working")


