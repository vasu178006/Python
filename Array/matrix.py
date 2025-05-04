row=int(input("enter the number of rows"))
col=int(input("enter the no. of cols"))
myArray=[]
print("enter the value row by row")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input("enter value")))
    myArray.append(a)
for i in range(row):
    for j in range(col):
        print(myArray[i],[j],end="")
    print()
