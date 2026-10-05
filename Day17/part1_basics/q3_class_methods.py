class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks= marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
        
    def is_passed(self):
        return self.marks >= 35
    
    
s1=Student("Giri", 45)
s1.display()
print("pass:", s1.is_passed())