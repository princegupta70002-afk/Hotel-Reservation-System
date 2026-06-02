class Employee :
    a = 1

    @classmethod
    def show(cls):
        print(f"Employee class attribute a: {cls.a}")

e = Employee()
e.a = 45
e.show()