# =============================================== Dog class  =======================================
class Dog:
    # constructor
    def __init__(self, name, age):
        self.Kingdom = "Animalia"
        self.name = name
        self.age = age


    @staticmethod  #for methods that do not require self and work at class level, @staticmethod decorator is used
    def hello():
        print("Hello EveryOne!")

    def bark(self):
        print(f"{self.name} is barking...")

# making object from class
dog1 = Dog("Cooper",6)
dog1.bark()
dog1.hello()
print(dog1.name, dog1.age, dog1.Kingdom)

# =============================================== Cat class  =======================================
class Cat:
    # constructor
    def __init__(self,name,age):
        self.Kingdom = "Animalia"
        self.speak = "Meow"
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is of age {self.age}. It belongs to {self.Kingdom} Kingdom"

Cat1 = Cat("Tom",14)
print(Cat1)
print(Cat1.name, Cat1.age, Cat1.Kingdom)

# =============================================== Duck class =======================================
class Duck:
    def __init__(self,name,age):
        self.speak = "Quack"
        self.name = name
        self.age = age

Duck1 = Duck("Bubbles",3)
print(Duck1) # in class, we have not defined __str__ method.so created object will look like this(not readable form)
print(Duck1.name, Duck1.age)

# animal-sound function
def animal_sound(animal):
    print(f"{animal.name} is saying {animal.speak}")

animal_sound(Cat1)
animal_sound(Duck1)

# ===================================== person class ==========================================
# inheritance
class Person:
    def __init__(self):
        print("creating person object...")

    def eat(self):
        print("I can eat food")

    def sleep(self):
        print("I can sleep")

    def walk(self):
        print("I can walk")
    
    def work(self):
        print("I am a person and I do nothing...")

person1 = Person()
person1.walk()
person1.eat()
person1.sleep()
person1.work()

class engineer(Person):
    def __init__(self):
        super().__init__()

    # over-writing function for child element 
    def work(self):
        print("hey! I am an engineer and I can work!")

eng1 = engineer()
eng1.eat()
eng1.work()

# ========================================= banking system =======================================================

class Account:
    def __init__(self,bal,acc,password):
        self.bal = bal
        self.acc = acc
        # creating private methods (start with double underscore __ ) that should not be accessible outside class
        self.__password = password
        # print(f"Your account password is {self.__password} . Do not share it with anyone!")
        print(f"New account created successfully for account number : {self.acc}")

    def debit(self,amount):
        self.bal -= amount
        print(f"you have debitted Rs. {amount} from your account {self.acc}.Remaining balance = {self.bal}")

    def credit(self,amount):
        self.bal += amount
        print(f"you have creditted Rs. {amount} in your account {self.acc}.Current balance = {self.bal}")

    def get_balance(self):
        print(f"Your current balance is {self.bal}")

# creating objects
newAcc1 = Account(1000,"abc123","123bnvhv")
newAcc1.debit(100)
newAcc1.credit(200)
newAcc1.get_balance()

newAcc2 = Account(1020,"aaa","21dwdwdcknl")
# delete keyword
del newAcc2.bal
del newAcc2
# print(newAcc2)
