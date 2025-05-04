n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i):
        print("*",end="")
        j=j+1
    i=i+1
    j=1
    print()
