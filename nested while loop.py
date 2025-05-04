n=int(input("enter the number"))
i=1
j=1
while(i<=n):
    while(j<=10):
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    j=1
print("exited")
