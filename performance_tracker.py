class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = sum(marks)/len(marks)

students_data = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

students = [Student(name, marks) for name, marks in students_data.items()]
average_marks = {s.name: round(s.average, 2) for s in students}
top_performer = max(students, key=lambda x: x.average).name

print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
