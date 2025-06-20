class Animal:
    def  __init__(self, name):
        self.name = name 
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
        def bark(self):
            print(f"{self.name} barks.")

d1 = Dog("Buddy")
d1.speak()
d1.bark()
        