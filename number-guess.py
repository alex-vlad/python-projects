"""
This is a dice game where the user guess a number and if that number is greater than the number from the dice, 
the user wins, if not, the machine wins
"""
from random import randint
from time import sleep

def get_user_guess(number_of_sides):
    """prompt the user for their guess"""
    max_value = number_of_sides * 2
    user_guess = int(input("Enter a number from 1 to " + str(max_value) + ":\n"))
    if user_guess > max_value:
      print(str(user_guess) + " is higher than " + str(max_value) +"\nTry again...")
      return get_user_guess(number_of_sides)
    else:
      return user_guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("The maximum possible value is: %s" % (max_val))
    sleep(1)
    user_guess = get_user_guess(number_of_sides)
    if user_guess > max_val:
      print("Your guess is invalid\nExiting...")
      return 
    else:
      print("Rolling...")
      sleep(2)
      print("First roll is: %d" % (first_roll))
      sleep(1)
      print("Second roll is: %d" % (second_roll))
      sleep(1)
      total_roll = first_roll + second_roll
      print("Total roll is: %d" % (total_roll))
      print("Result...")
      sleep(1)
      if user_guess > total_roll:
        print("YOU WON!!")
        return
      else:
        print("YOU LOST")
        return

roll_dice(6)
