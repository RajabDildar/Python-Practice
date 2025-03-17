class Engineer():
    def __init__(self,name):
        self.name = name
        print(f"Creating new engineer object...")

    def work(self):
        print(f"Hey I am an engineer and I can work...")

class promptEng():
    def __init__(self,name):
        self.name = name
        print(f"Creating new prompt engineer object...")

    def work(self):
        print(f"Hey I am a prompt engineer and I can work...") 

    def tools(self):
        print(f"I make prompts via chatGPT,deepseek and claude")   

# multiinheritance
class softwareEng(Engineer,promptEng):
    def __init__(self, name):
        super().__init__(name)
    
eng1 = softwareEng("Ahmed")
print(eng1)
eng1.work()
eng1.tools()

# =========================== classname =======================
class Person():
    name = "Anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
print(p1.name)
print(Person.name)
p1.changeName("Ali")
print(p1.name)
print(Person.name)

#  property decorator => used when value of an attribute depends on value of other attributes

class student():
    def __init__(self,math,eng,phy):
        self.math = math
        self.eng = eng
        self.phy = phy

    @property
    def calcPercentage(self):
        return (self.math + self.eng + self.phy) / 3
    
s1 = student(97,99,98)
print(s1.calcPercentage)

# now we will make changes to a subject number to see if the percentage is calculated again or not
s1.eng = 86
print(s1.calcPercentage)