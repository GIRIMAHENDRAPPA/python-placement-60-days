def square(x):
    return x*x
    return x*x

square_lambda = lambda x: x*x
print(square_lambda(5))


students = [("Aman", 12), ("Riya", 14), ("John", 8)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students) # Riya first


marks = [45, 80, 35, 90, 55]

passed = list(filter(lambda m: m >= 50, marks))
print(f"Passed marks: {passed}")

grace = list(map(lambda m: m+5, passed))
print(f"After grace: {grace}")