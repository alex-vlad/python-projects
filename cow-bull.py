from random import randint

number=str(randint(1000,10000))
print(number)
cows=0 
guess=1 

def game(num):
    cow=0 
    bulls=0 
    for i in range(0,4):
        if num[i]==number[i]:
            cow+=1 
        elif num[i] in number:
            bulls+=1
    return cow,bulls

while cows < 4:
    num = input("Guess:")
    if len(num) > 4 or len(num)<=3:
      print("invalid number")
    else:
      cow, bulls=game(num)
      print("Your cows",cow)
      print("Your bulls", bulls)
      if cow==4:
        print("You won and you hav {1}ows and {0}uess".format(cow,guess))
      else:
        guess+=1 
        print("Try again:")
