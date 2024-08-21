#Find Nth Fibo term (assume 1 and 2 as 1st 2 terms)

N = int(input("Enter a number: "))

term1 = 0
term2 = 1

fibo_array = []

count = 0

while count != N:
    term3 = term1 + term2
    term1 = term2
    term2 = term3

    fibo_array.append(term3)
    count += 1

print(f"The {N}th HemaChandra sequence number is: ",fibo_array[N-1])