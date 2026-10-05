class Student:
    def __init__(self, name, cgpa,backlogs):
        self.name = name
        self.cgpa = cgpa
        self.backlogs = backlogs

    def is_eligible(self):
        if self.cgpa >= 7.0 and self.backlogs == 0:
            return True
        return False
    
s1=Student("Giri", 8.5, 0)
s2=Student("Ravi", 6.5, 1)
    
print(f"{s1.name} is eligible: {s1.is_eligible()}")
print(f"{s2.name} is eligible: {s2.is_eligible()}")