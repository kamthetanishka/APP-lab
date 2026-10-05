# multilevel Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
f=Father("Ram",50)
f.display()    
super = "college"
class Son(Father):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
        print("Father's College:",super)
s=Son("Shiv",20,"Python","Blue")
s.display()


#Multiple Inheritance
class Father:   
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Mother:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Child(Father,Mother):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
c = Child("Shreyaa",19,"Python","Blue")
c.display()                        

# Hybrid Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Mother:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Child(Father,Mother):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
class GrandChild(Child):
    def __init__(self,name,age,language,clour,school):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour
        self.school = school

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
        print("School:",self.school)
c = GrandChild("Shreyaa",19,"Python","Blue","ABC School")
c.display()

#Herarchical Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Son(Father):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
p = Son("Shiv",20,"Python","Blue")
p.display()                                
                        