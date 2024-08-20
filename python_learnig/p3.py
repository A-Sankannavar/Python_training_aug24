#accept a number as input, say as X and define a logic to get a output say Y. The Input can be only 0 or 1 and the output must be 1 if input is 0 and viceversa.

X = int(input("Enter only 1 or 0: "))
if X==0 or X==1:
    Y=1-X
    print("input number: ",X,"\nOutput number: ",Y)
else:
    print("Invalid input")