class Student:
    def __init__(self):
        self.name="aman"
        self.__marks=90
    
    def show_marks(self):
        return self.__marks
    
s=Student()
print(s.name)
#print(s.__marks)
print(s.show_marks())