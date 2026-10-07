print(len("aman"))
print(len([1,2,3]))

class Dog:
    def speak(self):
        self.name="bhow bhow"
    
class Cat:
    def speak(self):
        self.name="meow meow"
        
animals=[Dog(),Cat()]
for a in animals:
    a.speak()