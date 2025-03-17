import os

f1 = open("sample1.txt","r")

""" data1 = f1.read()
print(data1) """

line1 = f1.readline()
print(line1)

f1.close()

# write mode
""" f2 = open("sample2.txt","w") #if file does not exist, it will be created

f2.write("This is a new line1")

f2.close() """

# appending text
f2 = open("sample2.txt","a") #if file does not exist, it will be created

f2.write("\nThis is a new line2")

f2.close()

# with syntax => closes file automatically after performing action
with open("sample1.txt","r") as f3:
    data2 = f3.read()
    print(f"data2 = {data2}") 

# deleting a file
# os.remove("sample3.txt")