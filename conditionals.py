age = int(input("Your age : "))
# conditional statements
if age>= 18:
    print("You are an Adult")
elif age >=13:
    print("You are a Teen")
else:
    print("You are a child") 

# checking light color
lightClr = input("Light color : ")
if(lightClr == "Red"):
    print("Please stop!")
elif(lightClr == "Yellow"):
    print("Get ready to move...")
elif(lightClr == "Green"):
    print("Move now!")
else:
    print("Sorry! Light is broken...")

# Taking input from user and printing it
username = input("username : ")
userage = int(input("age : "))
penprice = float(input("Pen price : "))
print(f"Hi! My name is {username} and I am {userage} years old. this pen costs ${penprice}")

# assigning grades to student according to their marks
marks = int(input("Your marks : "))
if(marks >= 90 and marks <=100):
    print("Congrats! you have got A grade.")
elif(marks >= 80 and marks < 90):
    print("Congrats! you have got B grade.")
elif(marks >= 70 and marks < 80):
    print("Congrats! you have got C grade.")
elif(marks >= 33 and marks < 70):
    print("Congrats! you have got D grade.")
else:
    print("Oops! you have got F grade.")  


# single line if ternary operator
speed = int(input("Current speed : "))
challan = "You will have to pay the challan amount" if(speed >= 100) else "You will NOT have to pay the challan amount"
print(challan)

food = input("What to eat today?")
print("Food is sweet") if (food == "cake") or (food == "jalebi") else print("Food is not sweet")

# clever if ternary operator
voterAge = int(input("Voter age : "))
vote = ("yes! you can vote.","No! you can NOT vote.")[voterAge < 18]
print(vote)

# even number checking
num1 = int(input("write a random number : "))
if (num1 % 2 == 0):
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

num2 = int(input("write random Number : "))
print(f"{num2} is multiple of 5") if(num2%5==0) else print(f"{num2} is NOT a multiple of 5")