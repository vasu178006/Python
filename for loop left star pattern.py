n=int(input("enter the number"))
i=1
j=1
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(" ",end="")
        j=j+1
    j=1
    for j in range(1,i+1):
        print("*",end="")
        j=j+1
    i=i=1
    j=1
    print()
r
