import array
n=int(input("enter the size of array"))
a=array.array('i',n*[0])
print("enter the values of n")
for i in range(0,n):
      a[i]=int(input("enter value"))
print("output")
for x in a:
      print(x)
      
