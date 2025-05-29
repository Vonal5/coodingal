#python programe to print a star pattern based on numbers of raw specialy by the user
#get the number of raw from user
n=int(input("enter the numer of raws: "))
#outer loop for each one 
for i in range (1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
