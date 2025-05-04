n=int(input("enter the number of rows"))
i=1
j=1
k=1
while(i<=n):
    while(j<=n-i+1):
        print(" ",end="")
        j=j+1
    j=1
    while(j<=k):
        print("*",end="")
        j=j+1
    i=i+1
    k=k+2
    j=1
    print()
