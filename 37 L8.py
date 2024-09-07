# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your average score is = ",sum/3)

s1 = Student("Aryan", [99,98,95])
s1.avg()
s1.marks = [95,95,95]
s1.avg()
