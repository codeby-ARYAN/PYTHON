# Search if the word "learning" exists in the file or not.
def search_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        if (word in data) :
            print("FOUND")
        else:
            print("Not Found")

i = input("word = ")
search_word(i)