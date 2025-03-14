# dictionaries are unordered(no index needed), mutable and don't allow duplicate keys

dict1 = {
    "name" : "Rajab",
    "cgpa" : 3.0,
    "subjects" : ["python", "javascript", "java"],
    "topics":("dictionaries", "sets"),
    "isPass":True,
    "age":17,
}

print(dict1)
print(dict1["name"]) # if key does not exist, it will return an error
print(dict1.get("name")) # if key does not exist, it will return None
dict1["name"] = "Ali"
dict1["height"] = 6.0
print(dict1)
print(dict1["subjects"][0])

null_dict = {}
print(null_dict)

stu1 = {
    "name":"Ahmed",
    "score":{
        "phy":77,
        "chem":66,
        "Bio":86,
    }
}

print(stu1["score"])
print(stu1["score"]["phy"])

# keys method gives all the keys in dictionary
print(stu1.keys())
print(f"list(stu1.keys()) = {list(stu1.keys())}") # typecasting returned value in list
print(f"list(stu1.values()) = {list(stu1.values())}")

# items method returns key value pairs in the form of tuples
print(f"stu1.items() = {stu1.items()}")

# update add new key value pairs in dictionary
updated_stu1 = {
    "city":"Faisalabad",
    "age":17
}

stu1.update(updated_stu1)
print(stu1)

# pq1

stu2 = {}
mathMarks = int(input("write maths marks : "))
stu2["Math"] = mathMarks
engMarks = int(input("write Eng marks : "))
stu2["Eng"] = engMarks
compMarks = int(input("write Comp marks : "))
stu2["Comp"] = compMarks
print(f"stu2 = {stu2}")