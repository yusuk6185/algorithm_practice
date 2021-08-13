# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

result = sorted(array, key=lambda student: student[1])

for student in result:
    print(student[0], end = ' ')

# input example
# 2
# 홍길동 95
# 이순신 77

# output example
# 이순신 홍길동