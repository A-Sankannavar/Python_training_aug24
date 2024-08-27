N = int(input("Enter the length of the string: "))
lis = []

for i in range(N):
    lis.append(input(f"Enter the {i+1}th element: "))

print("The list before soting is: ",lis)

def insertion_sort(N , lis):

    for i in  range (1,N):
        element = lis[i]
        j = i-1

        while j >= 0 and element < lis[j]:
            lis[j+1] = lis[j]
            j = j-1
        lis[j+1] = element

insertion_sort(N,lis)
print(lis)