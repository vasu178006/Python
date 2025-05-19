a={1,2,3,4,5,5,6,6,7,8,7}
b={2,3,4,5,65,4,32}
a.add(7)#adds elements to the sets
print(a)
print(len(a))#gives the length of the set
print(max(a))#gives the maximum eleemnt of the set
print(min(a))#gives the minimum element of the set
print(sum(a))#gives the sum of the set elements
a.clear()#clears the set
print(b.discard(5),b)#discard a element from the set,if doesnt exist no erroir msg
print(b.remove(3),b)#removes element from the set ,if doesnt exist no error msg is shown
print(b.pop())#removes random element fronm the set


