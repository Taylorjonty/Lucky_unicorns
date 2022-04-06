# ** component 3 (random tokens) v3
# format currency,
# Ensure odds favour the house - 10% chance of unicorn and 33% for each of donkey, zebra or horse

import random

tokens = ["unicorn",
          "horse", "horse", "horse",
          "donkey", "donkey", "donkey",
          "zebra", "zebra", "zebra"]
starting_balance = 100
balance = starting_balance

# Testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    # output
print(f"Starting balance = ${starting_balance:.2f}")
print(f"final balance = ${balance:.2f}")


