class Employee:
    language = "python" # this is a class attribute
    salary = 50000

    def getinfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Good Morning")


harry = Employee()
# harry.language = "javascript" #This is an instance atteibute
harry.getinfo()
#Employee.greet(harry)
