#Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers)

seq_size = int(input("Enter the size of the the HemaChandra sequence: "))

term1 = 0
term2 = 1

print(f"The first {seq_size} terms of HemaChandra sequence are: ")
for i in range(seq_size):
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    print(term3,end=' ')