#WAP to check if a list contains a palindrome of elements.
list = ["R","A","C","E","C","A","R"]
copylist = list.copy()
copylist.reverse()
print(list)
if copylist == list :
    print("Palindrome") 
else:
    print("Not Palindrome")

#palindrome = same meaning from both(front & reverse) sides of reading