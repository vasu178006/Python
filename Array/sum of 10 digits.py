import array
a=array.array('i',10*[0])
s=0
i=0
print("enter 10 values")
for x in range(0,10):
    a[i]=int(input("enter value"))
for n in a:
    s=s+n
print("output")
for n in a:
    print(n)
print("sum",s)
             
