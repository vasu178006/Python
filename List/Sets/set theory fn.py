a={1,2,3,4,5,6,7,8,9}
b={9,7,56,78,83,52,3,4,5}
print(a.intersection(b))#gives common element
print(a.union(b))#gives set of all elements
print(a.difference(b))#elements present in set 1 but not in set 2
print(a.issuperset(b))#checks if all elemnts of set 2 are present in set 1
print(a.issubset(b))#checks if all elemnts of set 1 are present in set 2
print(a.isdisjoint(b))#checks if the intersection of both sets=0 or not
print(a.intersection_update(b),a)#gets the intersection and updates set 1 with it
print(a.difference_update(b),a)
print(9 in a)#checks whether element exists in set or not
print( 10 not in a)
print(a is b)#checks whether both sets are pointing to same data or not