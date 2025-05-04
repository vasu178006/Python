import array
a=array.array('i',[1,2,3,4,5,6])
b=array.array('i',[7,8,9])
a.extend(b)
for n in a:
    print(n)
