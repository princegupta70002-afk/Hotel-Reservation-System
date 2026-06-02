class Employee:
    language = "python" # this is a class attribute
    salary = 50000

    def __init__(self,name ,language,salary):#dunder method which is automatically called 
        self.name = name 
        self.language = language
        self.salary = salary 

    def getinfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning")


harry = Employee( "Harry",120000,"javascript")
#harry.name = "harry"
print(harry.name,harry.salary,harry.language)

#rohal = Employee()

