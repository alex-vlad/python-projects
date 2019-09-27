"""
The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
"""

from random import randint
from time import sleep

# Options list which will not change
OPTIONS = ["R", "P", "S"]

# Messages to user
LOSE_MESSAGE = "\nYou Lost!"
WIN_MESSAGE = "\nYou Won!"

def decide_winner(user_choice, computer_choice):
    # This funciton takes 2 parameters and compare them to see who is the winner.
    print("\nYou chose:\n%s" % (user_choice))
    print("Computer chose...")
    sleep(1)
    print(computer_choice)
    user_choice_index = OPTIONS.index(user_choice)
    computer_choice_index = OPTIONS.index(computer_choice)
    if user_choice_index == computer_choice_index:
    # Set a draw if both indexes are the same
      sleep(1)
      print ("\nDRAW!")
    elif (user_choice_index == 0 and computer_choice_index == 2) or (user_choice_index == 1 and computer_choice_index == 0) or (user_choice_index == 2 and computer_choice_index == 1):
    # One condition to handle all the events where the user will win
      print(WIN_MESSAGE)
      return
    else:
      print(LOSE_MESSAGE)
      return

def play_RPS():
    user_choice =input("Select R for Rock, P for Paper, or S for Scissors\n")
    sleep(1)
    user_choice = user_choice.upper()
    if user_choice == "P" or user_choice == "R" or user_choice == "S":
    # Verify user's input. It it is invalid ask for it again.
      computer_choice = OPTIONS[randint(0,len(OPTIONS) - 1)]
      decide_winner(user_choice, computer_choice)
    else:
      print(user_choice + " is an invalid choice\nTry again...")
      return play_RPS()

print("Welcome to the Rock, Paper, or Scissors Game\n")
play_RPS()
