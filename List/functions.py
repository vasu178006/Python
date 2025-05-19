a = [1, 2, 3, 4, 5, 6, 4, 8]
b = [17, 18, 19]
c=[1,2,3,4,4,5,31,31,331,13,1,4]

print("Original list a:", a)

a.append(11)
print("After append(11):", a)  # Adds 11 at the end

a.append(b)
print("After append(b):", a)  # Appends entire list b as a single element

a.extend(b)
print("After extend(b):", a)  # Extends list a by adding elements of b

index_of_4 = a.index(4, 3)
print("Index of 4 starting from index 3:", index_of_4)

a.insert(3, 5)
print("After insert(3,5):", a)  # Inserts 5 at index 3

popped_element = a.pop(6)
print(f"Popped element at index 6: {popped_element}")
print("After pop(6):", a)

a.reverse()
print("After reverse():", a)

count_4 = a.count(4)
print("Count of 4 in a:", count_4)

c.sort()
print("After sort():", c)

a.clear()
print("After clear():", a)

print("Length of a after clear:", len(a))
