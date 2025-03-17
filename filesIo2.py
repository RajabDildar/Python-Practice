#practice questions
# pq1
""" with open("sample4.txt","w") as f:
    f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java") """

# updating data in file
""" with open("sample4.txt","r") as f1:
    data = f1.read()

updatedData = data.replace("Java", "Python")

with open("sample4.txt","w") as f2:
    f2.write(updatedData) """

with open("sample4.txt","r") as f1:
    data = f1.read()

output = data.find("learning")
print(output)