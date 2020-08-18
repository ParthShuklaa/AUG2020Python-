"""
Input the Name and Age of the user
Check if person can vote
Display Status

"""
name = input("Enter your Name\n")
print(type(name))
age = int(input("Enter your Age\n"))
print(type(age))
if age>= 18:
    print("Congratulations\t, you can vote!!")
else:
    print("Go and Watch POGO/Cartoon")
