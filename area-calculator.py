"""
In this project, we'll create a calculator than can compute the area of a given shape, as selected by the user. 
The calculator will be able to determine the area of the following shapes:
  Circle
  Triangle
"""

# Import the modules we are going to use
from math import pi
from time import sleep
  
def get_area():
    # This function gets the area of circles and triangles
    shape = input("Enter C for Circle or T for Triangle:\n")
    if shape.isalpha():
        # Check if the shape is a letter. If it is, set it to uppercase.
        shape = shape.upper()
        numberFlag = False
        # We are going to use this flag to check if the input for radius, bases, etc. are numbers.
        if shape == "C":
            # We get inside the circle's area logic
            while numberFlag == False:
                radius = input("Intert circle's radius:\n")
                if radius.isdigit():
                    # Check if the radius is a number. If it is, we continue with our logic and set the flag to True
                    radius = float(radius)
                    circle_area = pi * (radius ** 2)
                    print("Circle's area is: %.2f\n" % (circle_area))
                    numberFlag = True
                    return
                else:
                    # If radius is not a number we keep asking the user for the radius. (Using the loop)
                    print ("Enter a number.\nTry again...")
                    sleep(1)
                    numberFlag = False
                    # The flag is false so the we do the loop one more time.
            
        elif shape == "T":
            # We get inside the triangle's area logic
            while numberFlag == False:
                base = input("Insert triangle's base:\n")
                height = input("Insert triangle's height:\n")
                if base.isdigit() and height.isdigit():
                    # Check if base and height are numbers. If they are, continue with the logic.
                    base = float(base)
                    height = float(height)
                    triangle_area = (base * height) / 2
                    print("Triangle's area is: %.2f" % (triangle_area))
                    numberFlag = True
                    return
                else:
                    print("The base and height need to be numbers\nTry again...")
                    sleep(1)
                    numberFlag = False
        else:
            # The user input a letter but not a valid one...give them an other chance.
            print(shape + " is not a valid shape.\nTry again...")
            sleep(1)
            return get_area()
    else:
        # User input invalid data, ask for a valid input.
        print(shape + " is not valid, enter a letter.\nTry again...")
        sleep(1)
        return get_area()

# Call the funciton get_area() function.
get_area()
    
    
        
