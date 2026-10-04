import datetime

# 1. Current date time
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day)

# 2. Current date only
today = datetime.date.today()
print(today)

# 3. Calculate difference - Used in placement
dob = datetime.date(2003, 5, 15)
today = datetime.date.today()
age_days = today - dob
print(f"Days old: {age_days.days}")

# 4. Format date
print(now.strftime("%d-%m-%Y %H:%M:%S"))