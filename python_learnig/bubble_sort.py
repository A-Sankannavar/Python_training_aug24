N = int(input("Enter the length of the string: "))
lis = []

for i in range(N):
    lis.append(input(f"Enter the {i+1}th element: "))

print("The list before soting is: ",lis)

def bubble_sort(N , lis):

    for i in  range (N):
        for j in range (N-i-1):
            if lis[j] > lis[j+1]:
                temp = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = temp

bubble_sort(N,lis)
print("The list after soting is: ",lis)