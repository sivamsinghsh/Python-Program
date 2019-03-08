#rock paper scissor tow players game
import random

moves = ["rock", "paper", "scissors"]

keep_playing = "true"

while keep_playing == "true":
    cmove = random.choice(moves)
    pmove = input("What is your move: rock, paper or scissors?")
    print ("The computer chose",cmove)
    if cmove == pmove:
        print ("Tie")
    elif pmove == "rock" and cmove == "scissors":
        print ("congratulations to the winner Player wins")
    elif pmove == "rock" and cmove == "paper":
        print ("congratulations to the winner Computer wins")
    elif pmove == "paper" and cmove == "rock":
        print ("congratulations to the winner Player wins")
    elif pmove == "paper" and cmove == "scissors":
        print ("congratulations to the winner Computer wins")
    elif pmove == "scissors" and cmove == "paper":
        print ("congratulations to the winner Player wins")
    elif pmove == "scissors" and cmove == "rock":
        print ("congratulations to the winner Computer wins")










        



