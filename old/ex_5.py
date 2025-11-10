student = int(input("학생수:"))
studentList = []
for i in range(student):
    studentList.append(int(input("성적:")))

print(f"{student}명의 평균은 {sum(studentList)/student:.2f}")
ov = 0
for i in studentList:
    if i >=80:
        ov += 1


print(f"{student}명중 80점 이상은 {ov} 명이다")
