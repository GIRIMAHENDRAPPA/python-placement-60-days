# Week 1 Final - Combines Day01 to Day06
def add_record():
    name = input("Name: ")
    cgpa = input("CGPA: ")
    with open("placement_final.txt", "a") as f:
        f.write(f"{name} - {cgpa} - Placed\n")
    print("Added!")

def view_records():
    try:
        with open("placement_final.txt", "r") as f:
            print("\n--- Placement Records ---")
            print(f.read())
    except FileNotFoundError:
        print("No records yet")

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Enter: ")
    if ch == '1': add_record()
    elif ch == '2': view_records()
    else: 
        print("Week 1 Completed!")
        break