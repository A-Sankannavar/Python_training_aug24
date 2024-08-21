#Check if a number is Prime

sample_number = int(input("Enter a number: "))

flag = 0

for i in range(2,((sample_number)//2)+1):
    for j in range(2,((sample_number)//2)+1):
        if i*j==sample_number:
            flag = 1
            break

if flag == 0:
    print(sample_number,"is a Prime number")