import array
a=array.array('i',10*[0])
i=0
print("enter 10 values")
while(i<=9):
    a[i]=int(input("enter value"))
    i=i+1
print("output")
for n in a:
    print(n)
    
