#Bank Account Manager
"""Create a class called Account which will be an abstract class for three other classes
called CheckingAccount,SavingsAccount and BusinessAccount.
Manage debits from these accounts through an ATM style program."""

class Account:
    def __init__(self, name):
        self.name=name
class CheckingAccount(Account):
  def __init__(self,name,balance):
      Account.__init__(self,name)
      self.balance=balance
  def __repr__(self):
    return "This account belongs to %s and has %.2f" % (self.name,self.balance)
  def show_balance(self):
    print("Balance is %.2f"%(self.balance))
  def deposit(self,amount):
    if amount <0:
      print("Error")
      return
    else:
      print("Amount deposited %.2f" % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self,amount):
    if amount > self.balance :
      print("Error")
      return
    else:
      print("Amount withdraw %.2f"%(amount))
      self.balance-=amount
      self.show_balance()
class SavingsAccount(Account):
  def __init__(self,name,balance):
      Account.__init__(self,name)
      self.balance=balance
  def __repr__(self):
    return "This account belongs to %s and has %.2f" % (self.name,self.balance)
  def show_balance(self):
    print("Balance is %.2f"%(self.balance))
  def deposit(self,amount):
    if amount <0:
      print("Error")
      return
    else:
      print("Amount deposited %.2f" % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self,amount):
    if amount > self.balance :
      print("Error")
      return
    else:
      print("Amount withdraw %.2f"%(amount))
      self.balance-=amount
      self.show_balance()
class BusinessAccount(Account):
  def __init__(self,name,balance):
      Account.__init__(self,name)
      self.balance=balance
  def __repr__(self):
    return "This account belongs to %s and has %.2f" % (self.name,self.balance)
  def show_balance(self):
    print("Balance is %.2f"%(self.balance))
  def deposit(self,amount):
    if amount <0:
      print("Error")
      return
    else:
      print("Amount deposited %.2f" % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self,amount):
    if amount > self.balance :
      print("Error")
      return
    else:
      print("Amount withdraw %.2f"%(amount))
      self.balance-=amount
      self.show_balance()
      
"""my_account=CheckingAccount("Al", 2000)
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)"""
if __name__ == '__main__':
    SessionOn= True
    isCostumer= False
    def initialize():
        global alex_checking, lst, alex_savings, alex_business
        alex_checking=CheckingAccount("Alex",2000)
        alex_savings=SavingsAccount("Leo", 5000)
        alex_business=BusinessAccount("Kj", 1000)
        lst=[[alex_checking, "Alex"], [alex_savings, "Leo"], [alex_business,"Kj"]]
    initialize()
    while SessionOn is True:
        print("Welcome to ATM service.")
        name= input("Enter which account to use: ")
        for i in lst:
            if i[1]==name:
                isCostumer = True
                obj=i[0]
        #if isCostumer is True:
            while isCostumer is True:
                print ("\nHow may I help you?")
                print ("Press 1 for balance view.")
                print ("Press 2 for withdrawals")
                print ("Press 3 for deposit")
                print ("Press 4 to exit.")
                action=int(input("Enter your choice: "))
                if action == 1:
                    obj.show_balance()
                if action == 2:
                    amount=int(input("Enter amount: "))
                    obj.withdraw(amount)
                if action == 3:
                    amount=int(input("Enter amount: "))
                    obj.deposit(amount)
                if action == 4:
                    isCostumer= False
                    print("Have a nice day!")
        else:
            SessionOn=False
            print("Error. You dont have that account!")
