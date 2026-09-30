def generate_report(student_name, *marks, **details):
    total = sum(marks)
    avg = total / len(marks) if marks else 0
    print(f"\n--- Report for {student_name} ---")
    print(f"Total: {total}, Average: {avg:.2f}")
    print(f"Details: {details}")

    # Lambda for grade
    grade = (lambda a: "A" if a>=90 else "B" if a>=75 else "C" if a>=50 else "Fail")(avg)
    print(f"Grade: {grade}")

    if details.get('placed'):
        print(f"Placed in {details.get('company')} with {details.get('package')} LPA")

generate_report("Aman", 85, 90, 88, branch="AIML", placed=True, company="ServiceNow", package=14.97)
generate_report("John", 45, 50, 40, branch="CSE", placed=False)