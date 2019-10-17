class customer:
    bankname='DurgaBank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your balance is",self.balance)


    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print("your balance is ",self.balance)


print("Welcome to ",customer.bankname)
name=input("please enter your name")

c=customer(name)

while True:
    print("enter d for deposit\n enter w for withdraw\n e for exit")
    option=input("enter your opetion: ")
    if option.lower()=='d':
        amount=float(input("enter amount to deposit"))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input("enter amount to withdraw"))
        c.withdraw(amount)
    elif option.lower()=='e':
        break
    else:
        print("you entered wrong")

print("THanks")
    
