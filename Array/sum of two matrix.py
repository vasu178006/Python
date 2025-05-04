row=int(input("enter the no. of rows"))
col=int(input("entert he no. of cols"))
a=[]
print("enter the values of matrix a")
for i in range(row):
    aa=[]
    for j in range(col):
        aa.append(int(input("enter value")))
    a.append(aa)
b=[]
print("enter the values of matrix b")
for i in range(row):
    bb=[]
    for j in range(col):
        bb.append(int(input("enter the value")))
    b.append(bb)
s=[]
for i in range(row):
    ss=[]
    for j in range(col):
        ss.append(0)
    s.append(ss)
for i in range(row):
    for j in range(col):
        s[i][j]=a[i][j]+b[i][j]
print("matrix a")
for i in range(row):
    for j in range(col):
        print(a[i][j],end="")
    print()
print("matrix b")
for i in range(row):
    for j in range(col):
        print(b[i][j],end="")
    print()
print("matrix sum")
for i in range(row):
    for j in range(col):
        print(s[i][j],end="")
    print()
                  
