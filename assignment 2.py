n=int(input("enter the no. of rows"))
i=1
j=1
while(i<=n):
    j=1
    while(j<=n-i+1):
        print("*",end="")
        j=j+1
    i=i+1
    print()
i=1
while(i<=n):
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    i=i+1
    print()
        
