'''Program to print the Equi Lateral Triangle of N lines
    *
   ***
  *****
 *******
*********
'''
size = int(input("Enter the height of the triangle: "))
for i in range(size):
    print(' '*(size-i) + '*'*(i+1) + '*'*(i))