#Program tp print X shape of N lines

size = int(input("Enter the size of the square: "))
for i in range(1,size+1):
    for j in range(1,size+1):
        if(i==j or j==(size-i+1)):
            print('* ',end='')
        else:
            print('  ',end='')
    print('\n')