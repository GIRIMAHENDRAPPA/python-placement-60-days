def total_marks(*marks):
    print(f"marks tuple:{marks}")
    return sum(marks)

print(total_marks(80,90))
print(total_marks(80,90,95,85))
print(total_marks(50,60,70,80,90,100))

def add_students(*names):
    for name in names:
        print(f"added:{name}")

add_students("aman","riya","john")