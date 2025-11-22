N = int(input())
data = []

for _ in range(N):
    name = input()
    score = float(input())
    data.append([name, score])

data.sort(key=lambda x: x[1])

grades = sorted(set(score for name, score in data))
second_lowest_grade = grades[1]

second_lowest_students = [name for name, score in data if score == second_lowest_grade]

second_lowest_students.sort()

for student in second_lowest_students:
    print(student)
