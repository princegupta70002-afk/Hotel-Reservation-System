a = int(input("Enter a number:"))
b = int(input("Enter second number:"))

if (b == 0):

    raise ValueError("Hey , our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")