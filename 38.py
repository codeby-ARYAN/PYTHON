# Create Account class with 2 attributes - balance & account no. 
# Create methods for debit , creadit, &prinnt the balance.
class Account:
    def __init__(self,bal,acc): # constructor
        self.bal = bal
        self.acc = acc

    def debit(self,amount): # methods
        self.bal -= amount
        print("Rs.",amount,"was debited")
        print("Net balance = ", self.balance())

    def credit(self,amount):
        self.bal += amount
        print("Rs.",amount,"was credited")
        print("Net balance = ", self.balance())

    def balance(self):
        return self.bal
    
acc1 = Account(100000, 12345)  # object or instance
print("Available balance = ",acc1.bal)
acc1.debit(75000)
acc1.credit(6000)