fObj=open(r"C:\Users\vaska\OneDrive\Desktop\Python\file1.txt","r")
print("original file content is following")
for line in fObj:
    print(line)
print("Reading line from 4th position")
fObj.seek(4)
print(fObj.readline())
print("Give position of the file",fObj.tell())
fObj.close()
