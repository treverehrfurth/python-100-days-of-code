print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice
    # Small pizza (S): $15
    # Medium pizza (M): $20
    # Large pizza (L): $25
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bil based on their pepperoni choice
    # +$2
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


# todo: work out their final amount based on whether if they want extra cheese
    # +$1
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")