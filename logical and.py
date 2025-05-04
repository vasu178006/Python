a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>b and a>c):
    print('a is the greatest')
elif(b>c and b>a):
    print("b is the greatest")
elif(c>a and c>b):
    print("c is the greatest")
else:
    print("a,b,c are equal")
