# Write a recursive function to calculate the sum of first n natural number
def rec_sum(n):
    if n == 0:
        return 0
    else :
        return rec_sum(n-1)+n
# recursion = calling of function in same function    
n = int(input("n = "))
print("sum of first",n,"natural numbers =",rec_sum(n))