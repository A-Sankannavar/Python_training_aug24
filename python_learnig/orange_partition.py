N = int(input("Enter the number of the oranges: "))
oranges = []

for i in range(N):
    oranges.append(input(f"Enter the size of orange {i}: "))

print("Oranges before sorting: ",oranges)

def partition(N,lis):

    pivot = lis[N-1]
    for i in range (N):
        if pivot < lis[N-1-i]:
            temp = lis[N-1-i]
            del lis[N-1-i]
            lis.append(temp)

partition(N,oranges)
print("Oranges after sorting: ",oranges)

