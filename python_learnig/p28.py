#Print Prime numbers between M and N (M < N)

M = int(input("Enter the Starting range: "))
N = int(input("Enter the Ending range: "))


if M > N or M < 0:
    print("Invalid input")

else:

    flag = 0

    print(f"The prime numbers between {M} and {N} are: ")

    for sample in range(M,N+1):

        flag = 0

        for i in range(2,((sample)//2)+1):
            for j in range(2,((sample)//2)+1):
                if i*j == sample:
                    flag = 1
                    break
                
        if flag == 0:
            if sample == 0 or sample == 1:
                continue
            print(sample,end=' ')

