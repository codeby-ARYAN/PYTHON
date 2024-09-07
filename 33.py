# WAF that replaces all occurrences of "Java" with "Python" in above "practice.txt" file
def rep(x,y):
    with open("practice.txt","r") as f:  # r = read data from file
        data = f.read()
    new_data = data.replace(x, y)
    print(new_data)
    with open("practice.txt","w") as f:
        f.write(new_data)

rep("Java","Python")