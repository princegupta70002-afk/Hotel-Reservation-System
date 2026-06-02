class Employee:

     def __init__(self):
         print("Construtor of Employee")
     a = 1

class Programmer(Employee):
       def __init__(self):
        print("construtor of programmer") 
        b = 2  
class Manager(Programmer):
       def __init__(self):
          super().__init__()
          print("Construtor of Manager")
          c = 3


o = Employee()
print(o.a) # print the a attribute 


o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)
