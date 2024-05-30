import random

options = ["rock","paper","scissors"]
running = True
player_score=0
computer_score=0

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
     player = input("Enter a choice (rock,paper,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")
    
    if player == computer:
     print("It's a tie!")
    elif player =="rock" and computer =="scissors":
     print("you win!")
    elif player=="paper" and computer == "rock":
     print("you win!")
    elif player == "scissors" and computer == "paper":
     print("you win!")
    else:
     print("you lose!")
     player_score +=1
     print(player_score)
     computer_score +=1
     print(computer_score)

    play_again =input ("Play again? (y/n):").lower()
    if not play_again =="y":
        running = False
print("Thanks for playing")