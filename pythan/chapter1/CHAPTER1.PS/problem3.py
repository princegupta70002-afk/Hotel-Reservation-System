import os

# Ask user for a directory path
path = input("Enter the directory path: ")

# Check if the path exists
if os.path.exists(path):
    # List all files and folders in that directory
    contents = os.listdir(path)
    print("\nContents of the directory:")
    for item in contents:
        print(item)
else:
    print("The specified path does not exist.")

