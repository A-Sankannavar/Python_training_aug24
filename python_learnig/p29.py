#Find sum of the series: n + n(2) + n(3) + ..... m terms

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
sum = 0

for i in range (m):
    sum += n*(i+1)

print(f"The sum of sequence 'n + n(2) + n(3) + .....' upto {m} terms is: ",sum)