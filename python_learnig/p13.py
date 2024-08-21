#Program to find biggest (smallest) digit in a number

sample_number = int(input("Enter a number: "))
big = 0
for i in str(sample_number):
    if int(i)>big:
        big = int(i)
print("Biggest digit in the string is: ",big)
    