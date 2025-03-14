# strings are immutable
name = "Rajab Ali"

print(f"len(name) = {len(name)} and name[0] = {name[0]}")
print(name[0:4]) # slice
print(name[6:]) # slice
print(name[:9]) # slice
print(name[:len(name)]) # slice

# negative indexing => start from right(-1) and goes to left (-2,-3,-4,... so on)
print(name[-3:-1])

str1 = "i am learning python today"
print(str1.endswith("day")) #True
print(str1.capitalize()) #make first letter capital
print(str1.replace("learning","studying"))
print(str1.find("am"))  # returns 1st index of first occurence if exists. if it does not exist, we will get invalid -1 index
print(str1.count("n"))  # give number of occurences in a string