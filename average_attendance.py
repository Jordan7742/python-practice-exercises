"""
Average Attendance
Each row represents a student's attendance across 4 lessons (in minutes).
Calculates the average attendance per lesson slot across a 30-lesson term.
"""

students = [
    [60, 30, 45, 0],
    [180, 60, 0, 60],
    [200, 30, 0, 20],
    [60, 10, 15, 15],
    [100, 35, 30, 45],
]

total_minutes = sum(student[0] for student in students)
average = total_minutes / 30
print(average)
