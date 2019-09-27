import winsound, time

def sound():
    for i in range(2):
        for j in range(9): 
            winsound.MessageBeep(-1)
            time.sleep(2)
def alarm(t):
    print("Your time is " + str(t) +".")
    time.sleep(t)
    sound()

def choice(user_input):
    if user_input=='1':
        n=int(input("Hours: "))
        t=(h*60)*60
        alarm(t)
    elif user_input == '2':
        n=int(input("Mins: "))
        t=n*60
        alarm(t)
    elif user_input=='3':
        n=int(input('Sec:'))
        alarm(n)
    elif user_input == '4':
        h=int(input("Hours:"))
        m=int(input("Min:"))
        s=int(input("Sec:"))
        t=(h*60)*60+m*60+s
        alarm(t)
def main():
    print("What unit of time do you want to use?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
    user= input(": ")
    choice(user)
main()
    
    
    
        
