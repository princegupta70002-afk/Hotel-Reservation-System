class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("harry", 50000, 55000)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("rohan", 50000, 55000)
print(r.name, r.salary, r.pin, r.company)