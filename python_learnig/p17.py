#Program to Find Odd(Even) placed digits in a number

sample_number = int(input("Enter a number: "))
str_sample = str(sample_number)

print("The odd placed digits in a given number are: ")
for i in range(0,len(str_sample),2):
    print(str_sample[i],end=' ')