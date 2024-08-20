#Program to check if a number is Perfect Square


sample_number = int(input("Enter a number: "))
flag = 0
for i in range(2,sample_number):
    if i*i==sample_number:
        flag = 1
if flag == 1:
    print(f"{sample_number} is a perfect root")
else:
    print(f"{sample_number} is not a perfect root")

