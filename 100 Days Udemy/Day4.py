from random import randint

rps = ["Rock", "Paper", "Scissors"]

print("Let's play Rock Paper Scissors!")

my_num = int(input("Pick 0 for Rock, 1 for Paper or 2 for Scissors: "))

if my_num > 2 or my_num < 0:
    print("You typed an invalid number.")

else:
    computer_num = randint(0, 2)

    my_choice = rps[my_num]

    computer_choice = rps[computer_num]

    print(f"You chose {my_choice}, computer chose {computer_choice}.")

    if my_num == computer_num:
        print("It's a draw. Try again.")

    elif my_num == 0 and computer_num == 2:
        print("You win!")

    elif my_num == 2 and computer_num == 0:
        print("You lose.")

    elif my_num > computer_num:
        print("You win!")

    elif my_num < computer_num:
        print("You lose.")
