# Day14 - Report - File Handling
from analyzer import get_topper, get_average, get_placement_count, get_most_common_skill, get_failed_students

def generate_report():
    topper = get_topper()
    avg = get_average()
    placed, not_placed = get_placement_count()
    skill = get_most_common_skill()
    failed = get_failed_students()

    report_text = f"""
--- Student Data Analyzer Report - Day14 Project ---
Topper: {topper['name']} - {topper['marks']} marks
Average Marks: {avg:.2f}
Placed: {placed} | Not Placed: {not_placed}
Most Demanded Skill: {skill}
Failed Students: {failed}

"""
    print(report_text)

    # Save to file - Day06 logic
    with open("placement_report.txt", "w") as f:
        f.write(report_text)
    print("Report saved to placement_report.txt")

if __name__ == "__main__":
    generate_report()