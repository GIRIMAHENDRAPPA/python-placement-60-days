# PARENT CLASS - Person - 100% asked base
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def get_role(self):
        return "Person"

# CHILD CLASS - Student - inherits Person
class Student(Person):
    def __init__(self, name, age, roll_no, branch):
        super().__init__(name, age)  # 100% interview asks: What is super()?
        self.roll_no = roll_no
        self.branch = branch
    
    # Method Overriding - 100% asked
    def get_role(self):
        return "Student"
    
    # Child's own method
    def display_student(self):
        super().display()  # Call parent method
        print(f"Roll No: {self.roll_no}, Branch: {self.branch}, Role: {self.get_role()}")

# OBJECT CREATION - Placement Test
s1 = Student("Aman", 24, "12408XXX", "CSE AIML")
s1.display_student()

# CHECK INHERITANCE
print(isinstance(s1, Person))  # True - Asked in interview: Is Student a Person?
print(issubclass(Student, Person))  # True