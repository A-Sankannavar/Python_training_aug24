#Program to find Sum of even(odd) digits in a number

sample_number = int(input("Enter a number: "))
even_sum = 0
while sample_number>0:
    temp = sample_number%10
    if temp%2==0:
        even_sum = even_sum + temp
    sample_number=sample_number//10
print("Sum of even digits in number is: ",int(even_sum))

