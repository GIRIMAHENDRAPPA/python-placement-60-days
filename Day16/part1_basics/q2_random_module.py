import random

# 1. Random number
print(random.randint(1, 100))  # 1 to 100
print(random.random())         # 0 to 1 float

# 2. Random choice from list - VERY IMPORTANT for ML
students = ["Aman", "Rahul", "Priya", "ECE"]
print(random.choice(students))

# 3. Shuffle - used in ML data shuffle
nums = [1,2,3,4,5]
random.shuffle(nums)
print(nums)

# 4. Sample - Pick 2 random without repeat
print(random.sample(students, 2))