# Write a recursive function to print all elements in a list.(Hint : use list & index as parameters)
languages = ["Java","Python","C#","JavaScript"]
def list_el(list,i=0):
    if i == len(list):
        return
    print(list[i])
    list_el(list, i+1)

list_el(languages)