#Program to Print Math Table of A Number


sample_number = int(input("Enter a number: "))
print(f"Table of {sample_number}:\n")
for i in range(1,11):
    print(f"{sample_number} x {i} = {sample_number*i}")