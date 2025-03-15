# function definition
def greet(name):
    print(f"hello {name}!")

# function call 
greet("Ali")

def calcSum(a,b):
    print(a+b)

calcSum(2,4)

def calcAvg(a,b,c):
    avg = (a+b+c)/3
    print(avg)

calcAvg(2,3,4)

# printing length of a list
def lenCalc(a):
    print(f"len(a) = {len(a)}")

lenCalc([1,2,3,4,5])

# printing elements of a list in single line
def listEl(a):
    for el in a:
        print(el, end=" ")

listEl([1,2,3,4,5])

# finding factorial of n
n = 4
factorial = 1
for i in range(1,n+1):
    print(i)
    factorial *= i

print(f"factorial = {factorial}")

# converting usd to pkr

def converter(usd_val):
    pkr_val = usd_val*280
    print(f"{usd_val} USD to PKR = {pkr_val}")

converter(2)

# =================================== Recursion ==========================================
# recursive function
def show(n):
    if(n==0):  # the condition is called base case
        return
    print(f"n = {n}")
    show(n-1)
    print("end")

show(3)

# recurrence relation
# calculating factorial => fact(n) = fact(n-1) * n  (i.e, fact(3) = fact(2) * 3)
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
output = fact(5)
print(output)

# calculating sum of n numbers via recursive function
def calcSum2(n):
    if(n==0):
        return 0
    else:
        return n + calcSum2(n-1)


final_val = calcSum2(5)
print(f"sum via recursion = {final_val}")

sampleList = [11,22,33,44,55]
""" def listFunc(list,index):
    if(index == -1):
        return
    else:
        print(list[index],end=" ")
        listFunc(list, index-1)

listFunc(sampleList,len(sampleList)-1) """

def listFunc(list,index):
    if(index == len(list)):
        return
    else:
        print(list[index],end=" ")
        listFunc(list, index+1)

listFunc(sampleList,0)