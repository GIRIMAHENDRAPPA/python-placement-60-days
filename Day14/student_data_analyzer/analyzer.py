# Day14 - Analyzer Logic
from data import students
from collections import Counter

def get_topper():
    # Largest marks logic from Day09
    return max(students, key=lambda x: x["marks"])

def get_average():
    total = sum(s["marks"] for s in students)
    return total / len(students)

def get_placement_count():
    placed = [s for s in students if s["placed"] == True]
    return len(placed), len(students) - len(placed)

def get_most_common_skill():
    all_skills = []
    for s in students:
        all_skills.extend(s["skills"])
    return Counter(all_skills).most_common(1) # Day13 logic reused

def get_failed_students():
    # Using filter - for Day13 revision
    return [s["name"] for s in students if s["marks"] < 50]