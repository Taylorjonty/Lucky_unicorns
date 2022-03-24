show_instructions = ""
while show_instructions != "x":
    show_instructions = input("Have you played the game before: ").lower()
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
    elif show_instructions == "no" or show_instructions == "n":
        print("show instructions")
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered {show_instructions}")
