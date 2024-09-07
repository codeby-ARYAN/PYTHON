# WAF to find in which line of the file does the word "learning" occur first.
# Print- 1 if word not found
def find_line(word):
    data = True
    line = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()  # read line from data
            if (word in data):
                print(line)
                return
            line += 1
        else:
            print("-1")

l = input("word = ")
(find_line(l))