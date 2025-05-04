def fact(n):
     if(n>1):
         f=n*fact(n-1)
         return f
     else:
         return 1
n=int(input("enter the number"))
f=fact(n)
print("factorial",f)
