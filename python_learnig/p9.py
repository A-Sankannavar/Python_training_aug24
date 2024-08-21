#Program to Print Math Table of A Number


sample_number = int(input("Enter a number: "))
print(f"Table of {sample_number}:\n")
for i in range(1,21):
    print("%2d * %02d = %03d"%(sample_number,i,sample_number*i))