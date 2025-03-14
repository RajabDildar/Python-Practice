# Lists are mutable
stu1 = ["Ahmed", 92.8, 17, "Lahore"]
print(stu1)
stu1[0] = "Ali"
print(stu1)
print(len(stu1))

# list slicing
marks = [11,22,33,44,55]
print(marks[0:3])
print(marks[0:])
print(marks[-4:-1])

# list methods => return None but perform their function
list1 = [3,4,6,1,8,7,2,5]
print(f"list1 before append = {list1}")
list1.append(9)
print(list1.append(10)) # return None but perform operation
print(f"list1 after append = {list1}")
list1.sort()  # arrange list in ascending order
print(f"list1 after sort = {list1}")

list2 = ["a","e","f","b","c","d"]
list2.sort()
print(f"list2 after sorting in ascending order = {list2}")
list2.sort(reverse=True)
print(f"list2 after sorting in descending order = {list2}")

list3 = ["a","e","f","b","c","d"]
list3.reverse()
print(f"list3 after reversing = {list3}")

# insert element at index 
list4 =  [11,22,33,44,55]
list4.insert(1,101)
print(f"list4 after inserting = {list4}")

# remove method removes first occurence of element
list5 =  [11,22,33,44,55]
list5.remove(22)
print(f"list5 after removing = {list5}")

# pop method removes value at index 
list6 = [11,22,33,44,55]
list6.pop(2) # remove value at 2 index (i.e, 33)
print(f"list6 after pop = {list6}")

# ==================  Tuples => built in datatype, immutable like strings =========================
tup1 = (1,2,3,4,5,4,4)
print(f"tup1 = {tup1}")
print(type(tup1))

# tup1.index(el) returns indx of first occurence
print(f"4 in tup1 exists at index = {tup1.index(4)}")
print(f"4 in tup1 exists {tup1.count(4)} times")

tup2 = (1,) # for tuples having single value, writing comma at end is compulsory
print(type(tup2))

# practice set1
""" movie1 = input("Enter your fav movie 1 : ")
movie2 = input("Enter your fav movie 2 : ")
movie3 = input("Enter your fav movie 3 : ")

allMovies = [movie1,movie2,movie3]
print(allMovies) """

# pq2

list7 = [1,2,3,2,1]
list7_copy = list7.copy()
list7_copy.reverse()
print("Palindrome") if(list7_copy == list7) else print("NOT Palindrome")