#Program to Find count of digits of a number

sample_number = int(input("Enter a number: "))
count = 0
while int(sample_number)>0:
    count = count + 1
    sample_number=sample_number/10
print("Count of digits in number is: ",count)