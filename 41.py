# Create a class called Order which stores item & its price.
# use dunder function __gt__() to convey that : order1>order2 ,if  price of order1 > price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2): #gt = greater than // POLYMORPHISM
        return self.price > odr2.price

odr1 = Order("pizza", 99)
odr2 = Order("burger", 89)

print(odr1 > odr2)  #condition check