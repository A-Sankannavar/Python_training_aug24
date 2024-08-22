'''Find Nth term of the series:
1 2 2 3 3 5 5 7 8 11 13 13'''

N = int(input("Enter a number: "))
spe_series = []
spe_count = 0
spe_flag = 0

#Fibo prerequisits:
term1 = 0
term2 = 1

#Prime prerequisits:
sample = 2

#Main loop
while spe_count != N:

    #Fibo sequence addition

    if(spe_flag == 0):

        term3 = term1 + term2
        term1 = term2
        term2 = term3

        spe_series.append(term3)

        spe_count += 1    
        spe_flag = 1

    #Prime number addition

    elif(spe_flag == 1):

        
        pr_flag = 0

        while pr_flag == 0:

            flag = 0

            for i in range(2,((sample)//2)+1):
                for j in range(2,((sample)//2)+1):
                    if i*j==sample:
                        flag = 1
                        break
    
            if flag == 0:
                spe_series.append(sample)
                pr_flag = 1

            sample += 1
        
        spe_count += 1
        spe_flag = 0

print(f"The {N}th number in the sequence is: ",spe_series[N-1])