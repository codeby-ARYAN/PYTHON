#USING for loop, Print the elements of the following list:
nums  = [1,4,9,16,25,36,49,64,81,100]
for el in nums :
    print(el)

#search for number x in following tuple using for loop    
nums  = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter x = "))
for el in nums :
    if x == el :
        print("x is found")
        break
else :
     print("x is not found")
    
         



