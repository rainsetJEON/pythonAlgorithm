# p.180 성적이 낮은 순서로 학생 출력하기

# 계수 정렬과 기본 정렬 라이브러리를 이용한 답안 예시

 # n 입력 받기
n = int(input())

 # n명의 학생 정보를 입력받아 리스트에 저장
array = [] 
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

 # 키를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

 # 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')



# 람다 함수식
'''
lamda 매개변수 : 표현식

ex) (lamda x,y : x+Y)(10,20)
>> 30
'''

