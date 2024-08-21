#Find sum of the sries: n - n2/3 + n4/5 - n8/7 .... m terms (1<m<10)

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

sum = n
flag = 0

numerator = 1
denominator = 1

for i in range (m-1):

    numerator = numerator*2
    denominator = denominator+2

    if flag == 0:
        sum = sum - n*(numerator/denominator)
        flag = 1
    
    elif flag == 1:
        sum = sum +n*(numerator/denominator)
        flag = 0

print(f"The sum of sequence 'n - n2/3 + n4/5 - n8/7 ....' upto {m} terms is: ",sum)