class Employee:
    language = "py"#THIS is a class attribute
    salary = 50000


harry = Employee()
harry.name = "Harry" #This is an instance attribute   print(harry.language,harry.name,harry.salary)
print( harry.name ,harry.language, harry.salary)


rohan = Employee()
rohan.name = "Rohan Rono Robinson" 
print( rohan.name ,rohan.language, rohan.salary)


 #here name is instaance attribute and salary and language is class attribute as they directly belong to the class