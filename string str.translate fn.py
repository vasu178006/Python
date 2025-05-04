a="sring is immutable"
print('string= ',a)
trans=str.maketrans("aeiou","12345")
print("ASCII values that will be deleted =",trans)
print("translating of string=",a.translate(trans))
