print("Hello World!")

# variables
name = "Rajab Ali"
age = 17
institute = "UAF"
print(f"type of name = {type(name)} and type of age = {type(age)}")
# print("Welcome", name, "of age", age, "from your institute", institute)
print(f"Welcome {name} of age {age} from your institute {institute}")

# python is case sensitive
price = 200
Price = 300
print(price)
print(Price)

# type conversion => converting one datatype to another
print(str(price))
a = "22"
print(int(a) + 5)  # output should be 27

# Arithmetic operators
num1 = 22
num2 = 11
sum1 = num1 + num2
diff1 = num1 - num2
print(sum1)
print(diff1)
print(f"num2 ** 2 = {num2 ** 2}")  # output should be 11**2 = 121

# expressions execution
A,B = 2,3
Txt = "Ali"
print(A*Txt*B)  # the output should be 2*3 = 6 times "Ali" printed because when we multiply an integer with string, the string repeats itself according to that integer value

C,D = "2",3
Txt2 = "@"
print((C+Txt2)*D)  # the output should be 2@2@2@


print(7 / 3)  # Output: 2.333...  
# integer division is same as floor in math
print(7 // 3) # Output: 2  (// => integer division is used when we dont want floating value in answer)

# when // or any other operator is used with floats, the result will be float
print(7.0 // 3)   # Output: 2.0  
print(10.5 // 3)  # Output: 3.0  
print(10.5 * 2)   # Output will be 21.0 (floating value)

"""This is 
a multiline
comment in python"""

