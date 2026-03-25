file = open('grades.txt', 'r')
lines = file.readlines()
grades = []

def grade_to_gpa(grade):
    if grade >= 90:
        return 4.0
    elif grade >= 80:
        return 3.0
    elif grade >= 70:
        return 2.0
    elif grade >= 60:
        return 1.0
    else:
        return 0.0

while True:
    coursework = float(input("Enter coursework grade (20%): "))
    assessment = float(input("Enter assessment grade (80%): "))
    final = coursework * 0.2 + assessment * 0.8
    grades.append(final)
    done = input("Type 'done' to finish or press Enter to add another class: ")
    if done == 'done':
        break

average = sum(grades) / len(grades)
gpas = [grade_to_gpa(g) for g in grades]
average_gpa = sum(gpas) / len(gpas)

print(f'Average grade: {average:.2f}%')
print(f'Average GPA: {average_gpa:.2f}')