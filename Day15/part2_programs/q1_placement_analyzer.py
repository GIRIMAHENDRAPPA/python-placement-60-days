def filter_eligible_students(min_cgpa, *students):
    
    eligible = list(filter(lambda s: s['cgpa'] >= min_cgpa, students))
    return eligible

s1 = {'name': 'Aman', 'cgpa': 8.5, 'branch': 'AIML'}
s2 = {'name': 'Riya', 'cgpa': 7.2, 'branch': 'CSE'}
s3 = {'name': 'John', 'cgpa': 9.1, 'branch': 'AIML'}

result = filter_eligible_students(8.0, s1, s2, s3)
print("Eligible for ServiceNow (8+ CGPA):")
for s in result:
    print(f"{s['name']} - {s['cgpa']}")

