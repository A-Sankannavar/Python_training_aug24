#Program to Find Odd placed Even digits in a number


sample_number = int(input("Enter a number: "))
str_sample = str(sample_number)

print("The odd placed even digits in a given number are: ")
for i in range(0,len(str_sample),2):
    if int(str_sample[i])%2==0:
        print(str_sample[i],end=' ')