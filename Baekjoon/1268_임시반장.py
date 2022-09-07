N = int(input())

students = []
for i in range(N):
    students.append(list(map(int,input().split())))

student_count_list = []
for i in range(N):
    student_count = []
    choice_student = students[i]
    for j in range(5):
        for k in range(N):
            if choice_student[j] == students[k][j]:
                student_count.append(k)
    student_count = set(student_count)
    student_count = list(student_count)
    student_count_list.append(len(student_count))

print(student_count_list.index(max(student_count_list))+1)