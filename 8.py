#WAP to find the greatest of 3 numbers entered by user
a = float(input("num1 = "))
b = float(input("num2 = "))
c = float(input("num3 = "))
if (a>b and a>c):
    print("num1 is greatest")
elif (b>c):
    print("num2 is greatest")
else :
    print("num3 is greatest")    
