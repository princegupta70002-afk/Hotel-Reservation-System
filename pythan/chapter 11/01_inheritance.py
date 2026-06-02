class Employee:
    company = "ITC"
    def show (self):
        print("Welcome to", self.company)
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")



class Programmer (Employee):
    company = "ITC Infotech"
    def ShowLanguage(self):
        print(f"The name of the Programmer is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

print(a.company,b.company)