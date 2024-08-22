#Find sum of the series: 1 - n + n2 - n3 .... m terms

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

sum = 1
flag = 0

for i in range (m-1):

    if flag == 0:
        sum = sum - n**(i+1)
        flag = 1
    
    elif flag == 1:
        sum = sum + n**(i+1)
        flag = 0

print(f"The sum of sequence '1 - n + n2 - n3 ....' upto {m} terms is: ",sum)