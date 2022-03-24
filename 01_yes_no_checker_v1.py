# Ask the user if they have played before
show_instructions = input("have you played this game before").lower()

# If they answer yes, program continues
if show_instructions == "yes":
    print("program continues")
# If they answer no, output play instructions
elif show_instructions == "no":
    print("display instructions")
# Other wise show error
else:
    print("Please answer yes or no")

print(f"you entered {show_instructions}")
