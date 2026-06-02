class Employee:
    company = "ITC"
    name = "Default Employee"
    def show (self):
        print("Welcome to", self.company)
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class coder:
    language  = "python"
    def ShowLanguage(self):
        print(f"out of all the language here is your language:{self.language}")


class Programmer (Employee , coder):
    company = "ITC Infotech"
    def ShowLanguage(self):
        print(f"The name of the Programmer is {self.company} and the language is {self.language}")


a = Employee()
b = Programmer()


b.show()
b.ShowLanguage()
b.ShowLanguage()
