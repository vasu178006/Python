fObj=open(r"C:\Users\vaska\OneDrive\Desktop\Python\file1.txt","r")
d=fObj.readlines()
print("Content of the file=",d)
print("Type of data=",type(d))
fObj.close()
print("file is closed")

