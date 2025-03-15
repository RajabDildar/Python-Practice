# range() give sequence of numbers which start from zero by default
for i in range(5):  #range(stop)
    print(i)

for i in range(0,5):  #range(start, stop)
    print(i)

for i in range(0,5,2):  #range(start, stop, stepsize)
    print(i)

# to write a thing in which nothing to do, pass statement is used
for i in range(5):
    pass

# lists
fruits = ["apple", "cherry", "banana"]
print(fruits)

for fruit in fruits:
    print(fruit)
else:
    print("all fruit names printed successfully!")

count = 0
while count <5:
    print(count)
    count += 1

# creating table
n = int(input("write number : "))
x = 1
while x<=10:
    print(f"{n} * {x} = {n*x}")
    x+=1

# printing elements in the loop
list1 = [11,22,33,44,55]
j = 0
while j<len(list1):
    print(f"list[{j}] = {list1[j]}") 
    j+=1

# searching a value in tuple
tup1 = [11,22,33,44,55]
k=0
while k<len(tup1):
    if(tup1[k] == 33):
        print(f"33 found at index = {k}")
        break
    print("searching...")
    k+=1

h = 0
while h<=5:
    if(h==3):
        h+=1
        continue
    print(h)
    h+=1

# calculating sum of numbers
sum = 0
g=1
num = int(input("write number to get sum : "))
while g<=num:
    sum += g
    g += 1

print(f"sum = {sum}")

# calculating factorial of numbers
factorial = 1
f=1
num2 = int(input("write number to get factorial : "))
while f<=num2:
    factorial *= f
    f += 1

print(f"factorial = {factorial}")