my_name="Giri Mahendra"
my_branch="M.Tech AIML"
my_cgpa=8.09

f=open("student.txt","w")
f.write(f"Name:{my_name}\n")
f.write(f"Branch:{my_branch}\n")
f.write(f"CGPA:{my_cgpa}\n")
f.close()
print("student.txt written")