print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

step1 = input(
    'You\'re at a cross road. Where do you want to go?\n   Type "left" or "right" '
).lower()

if step1 == "right":
    print("Game over.")
elif step1 == "left":
    step2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n   "
        'Type "wait" to wait for a boat. Type "swim" to swim across. '
    ).lower()

    if step2 == "swim":
        print("Game over.")
    elif step2 == "wait":
        step3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\n   "
            "One red, one yellow and one blue. Which colour do you choose? "
        ).lower()

        if step3 == "red" or step3 == "blue":
            print("Game over.")
        elif step3 == "yellow":
            print("You win!")
