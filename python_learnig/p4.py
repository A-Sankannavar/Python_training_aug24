# prgram to accept 3 distinct numbers and find smallest amoung them

my_number1 = int(input("Enter the First number: "))
my_number2 = int(input("Enter the Second number: "))
my_number3 = int(input("Enter the Third number: "))
min=0

if(my_number1==my_number2 or my_number1==my_number3 or my_number3==my_number2 ):
    print("The numbers must be distinct")
else:
    if(my_number1<my_number2):
        min=my_number1
    else:
        min=my_number2
    if(min>my_number3):
        min=my_number3

print(f"{min} is the smallest number amoung given 3 numbers")


