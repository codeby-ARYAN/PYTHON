# WAF to print the elements of a list in a single line.(list is the parameter)
subjects = ["mathematics","physics","PPS","mechanical","soft skills","electrical"]
languages = ["Java","Python","C#","JavaScript"]

def pr_element(a):
    for item in a:
        print(item, end =" ")
pr_element(subjects)