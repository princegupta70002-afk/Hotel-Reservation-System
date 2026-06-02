Marks1 = int(input("Enter Marks 1:"))
Marks2 = int(input("Enter Marks 2:"))
Marks3 = int(input("Enter Marks 3:"))


#Check for total percentage 

total_percentage =(100*( Marks1 +Marks2 + Marks3))/300

if(total_percentage >=40 and Marks1>=33 and Marks2>=33 and Marks3>=33):
  print("You are passed :",total_percentage)

else:
    print("You failed , try again year :" , total_percentage)  