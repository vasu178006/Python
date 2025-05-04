import array
a=array.array('i',[1,2,3,4,5])
for n in a:
    print(n,a.buffer_info())
