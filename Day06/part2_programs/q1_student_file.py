f=open("records.txt","w")
for i in range(3):
    name=input(f"Enter name{i+1}:")
    cgpa=input(f"Enter CGPA{i+1}:")
    f.write(f"{name}-{cgpa}\n")
f.close()
print("Records saved to records.txt")