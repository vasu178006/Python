import array
a=array.array('i',5*[0])
i=0
print("enter 5 values")
while(i<=4):
    a[i]=int(input("enter the values"))
    i=i+1
print("unsorted array")
for n in a:
    print(n)
i=0
while(i<=3):
    j=i+1
    while(j<=4):
        if(a[i]>a[j]):
            a[i],a[j]=a[i],a[j]
        j=j+1
    i=i+1
print("sorted array")
for x in a:
    print(x)
        
        
