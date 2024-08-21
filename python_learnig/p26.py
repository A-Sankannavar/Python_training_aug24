#Find the Nth Prime number

N = int(input("Enter a number: "))

prime_array = []
sample = 2
count = 0

while count != N:

    flag = 0

    for i in range(2,((sample)//2)+1):
        for j in range(2,((sample)//2)+1):
            if i*j==sample:
                flag = 1
                break
    
    if flag == 0:
        prime_array.append(sample)
        count += 1

    sample += 1

print(f"The {N}th prime number is: ",prime_array[N-1])