import random
#Rock = 1, Paper = 2, Scissors = 3

print("\nWelcome to the Thunderdome!\n")
print("Rules of play:\nScissors slices Paper\nRock crushes Scissors\nPaper suffocates Rock")
while True:
    player_choice = input("\nLay down your best, enter 1 (Rock), 2 (Paper), 3 (Scissors), or q (quit)\n")
    computer_choice = random.randint(1,3)
    if player_choice.lower() == "q":
        break 
    elif int(player_choice) == 1:
        if computer_choice == 1:
            print("Computer's Choice: Rock\nDraw! How dare you rock my rock. Let's go again.")
        elif computer_choice == 2:
            print("Computer's Choice: Paper\nYou lost! You know the rules of the game right? Objective is not to lose in case you were wondering!")
        elif computer_choice == 3:
            print("Computer's Choice: Scissors\nYou won! Drats! I just got these scissors at Staples now they're all scuffed up from your rock. Let's play again.")
    elif int(player_choice) == 2:
        if computer_choice == 1:
            print("Computer's Choice: Rock\nYou won! I felt like a meatball getting saran wrapped after dinner. Drats! Let's go again!")
        elif computer_choice == 2:
            print("Computer's Choice: Paper\nDraw! You would throw paper when I throw paper copycat. Let's go again!")
        elif computer_choice == 3:
            print("Computer's Choice: Scissors\n You lost! I just made a bag of confetti out of you chump. Care to lose again?")
    elif int(player_choice) == 3:
        if computer_choice == 1:
            print("Computer's Choice: Rock\nYou lost! I just rocked you to sleep, Stallone would be proud. Let's go again.")
        elif computer_choice == 2:
            print("Computer's Choice: Paper\nYou won! Noooooo I had dreams of becoming a paper plane, you cut my wings off you heathen. Let's go again.")
        elif computer_choice == 3: 
            print("Computer's Choice: Scissors\nDraw! You're suppose to zig when I zag, we both zigged on that one! Let's go again.")
    else:
        print("\nDidn't recgonize input, please enter again. Input must be 1,2,3 or q!")



