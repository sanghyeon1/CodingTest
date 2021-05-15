n = int(input("Input the number of student : "))
student_info = []
for i in range(n):
    student_info.append(input().split())

for i in range(n):
    j = i+1
    for j in range(n):
        if j >= n:
            break
        if int(student_info[i][1]) >= int(student_info[j][1]):
            continue
        else:
            temp = student_info[j]
            student_info[j] = student_info[i]
            student_info[i] = temp

for i in range(n):
    print(student_info[i][0], end='')
