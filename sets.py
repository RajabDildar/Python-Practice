# sets elements are immutable. we cannot store mutable datatypes like lists and dictionaries in sets
# sets are collection of unordered and distinct items. each element in sets must be unique and immutable
# duplicate values in sets are ignored
# sets => mutable (i.e, we can add or remove elements in a set)
# set elements are immutable (can not be changed)
set1 = {1,2,3,3,"hello", "world"}
print(set1)
print(type(set1))
print(len(set1))

# creating empty set
set2 = set()
print(type(set2))

set2.add(1)
set2.add(2)
set2.add(3)
print(set2)
set2.remove(3)
print(set2)

set3 = {1,2,3}
set3.pop() # removes a random value
print(f"set3 = {set3}")
set3.clear()
print(f"set3 = {set3}")

# ==================================Union and Intersection ==============================
set4 = {1,2,3}
set5 = {3,4,5}
unionSet = set4.union(set5)
print(f"unionSet = {unionSet}")
interSet = set4.intersection(set5)
print(f"interSet = {interSet}")

# pq2
set6 = {"python", "java", "c++", "python", "java","python", "javascript","java", "c++", "c"}
print(f"len(set6) = {len(set6)}")

# saving 9 and 9.0 both in set
set7 = {"9",9.0}
print(set7)