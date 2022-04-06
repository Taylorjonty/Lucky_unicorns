# ** component 3 (random tokens) v4
# Calculate percentage's to ensure the odds favour the house
# 5% unicorns, 30% donkey, and the rest 65% horse/zebra


import random

starting_balance = 100
balance = starting_balance

# Testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

    # adjust balance
    if number <= 5:
        token = "unicorn"
        balance += 4
    elif number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= .50
        else:
            token = "horse"
            balance -= .50

# output
    print(f"Token: {token}. Balance: ${balance:.2f}")

print()
print(f"Starting balance = ${starting_balance:.2f}")
print(f"final balance = ${balance:.2f}")


