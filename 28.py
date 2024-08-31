# WAF to find the factorial of n.(n is the parameter)
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print("Factorial =",f)

fact(5)