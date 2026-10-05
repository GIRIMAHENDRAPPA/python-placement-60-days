class Student:
    def __init__(self, name,roll):
        self.name=name
        self.roll=roll
        print(f"Constructor is called for {name}")
    
    
s1=Student("Giri",101)
s2=Student("Ravi",102)
print(s1.name,s1.roll)
print(s2.name,s2.roll)