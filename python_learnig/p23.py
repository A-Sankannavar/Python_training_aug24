#Program to Print X shape inside Hollow Square

size = int(input("Enter the size of the square: "))
for i in range(1,size+1):
    for j in range(1,size+1):
        if(i==1 or i==size or j==1 or j==size or i==j or j==(size-i+1)):
            print('*   ',end='')
        else:
            print('    ',end='')
    print('\n')