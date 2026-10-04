# Day16 P2 Q2 - Age Calculator using datetime
import datetime

def calculate_age(birth_year, birth_month, birth_day):
    dob = datetime.date(birth_year, birth_month, birth_day)
    today = datetime.date.today()
    
    age = today.year - dob.year
    # Check if birthday not yet come this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    
    # Days
    total_days = (today - dob).days
    
    return age, total_days

# Input
y = int(input("Enter birth year: "))
m = int(input("Enter birth month: "))
d = int(input("Enter birth day: "))

age, days = calculate_age(y, m, d)
print(f"You are {age} years old")
print(f"You are {days} days old")