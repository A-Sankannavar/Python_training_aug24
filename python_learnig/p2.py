#Read a number from a user and check if it is an Even number or not

my_number = int(input("Enter a number: "))
print(type(my_number))
if(my_number%2==0):
    print(f"{my_number} is an Even number")
else:
    print(f"{my_number} is not an Even number") 