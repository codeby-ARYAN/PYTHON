#Search for a number x in this tuple using loop: 
nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter x = "))
i = 0
while i < len(nums) :
    if x == nums[i] :
        print("x is found at index",i)
        break    
    i += 1
    if i == len(nums):
        print("x is not found.")