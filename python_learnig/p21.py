#Program to print a Hollow Square of N lines
size = int(input("Enter the size of the square: "))
for i in range(size):
    for j in range(size):
        while(i==0 or j==0 or i==size or j==size):
            print('*  ',end='')
    print('\n')