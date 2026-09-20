def placement_status(cgpa,attendance=75):
    if cgpa >= 7 and attendance > 75:
        return "Eligible for placement"
    return "not placed"

print(placement_status(8, 90))  # Eligible for placement
print(placement_status(6, 80))  # not placed