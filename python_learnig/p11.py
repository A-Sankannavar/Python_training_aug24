#program to find sum of digits of a number
sample_number = int(input("Enter a number: "))
sum = 0
while sample_number>0:
    temp = sample_number%10
    sum = sum+temp
    sample_number=sample_number/10
print("Sum of digits in number is: ",int(sum))