# if문

money = 2000
if money >= 3000:
    print("get a cab")

else :
    print("walk")


money2 = 3000
card = True
if money >= 4000 or card:
    print("get a cab")
else :
    print("walk")


text1 = 1 in [1,2,3]
text2 = 1 not in [1,2,3]
text3 = 'j' not in 'python'

for i in text1,text2,text3 :
    print(i)


pocket = ['paper', 'coin', 'smartphone']
card = True
if 'money' in pocket:
    print('get a cab')
elif card:
    print('get a bus')
else:
    print('walk')

# pass는 아무것도 출력하지 않는다.
list1 = ['a', 'b', 'c']
if 'd' in list1:
    pass
else:
    print("'d'is not in list")

# 조건문 표현식 -1
score = 60
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

# 조건문 표현식 -2
message = "success" if score >= 60 else "failure"
print(message)

# p118 연습문제 1번
a = "Life is too shrot, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')

    
# while문
treeHit = 0
while treeHit <5:
    treeHit = treeHit + 1
    print("treeHit = %d" % treeHit)
    if treeHit == 5:
        print("yes! we made it!")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : 
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기
# coffee
coffee = 10
money = 300
while money:
    print("Here you are")
    coffee = coffee -1
    print("남은 커피 = %d 개" % coffee)
    if coffee == 0:
        print("sold out")
        break

# coffee2
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("Here you are")
        coffee = coffee -1
    elif money > 300:
        print("here is your change %d" % (money -300))
        coffee = coffee -1
    else:
        print("your balance is low")
        print("남은 커피 = %d 개" % coffee)
    if coffee == 0:
        print("sold out")
        break
# ㄴ> 조건에 맞지 않으면 while문을 빠져 나간다.

# while문 맨 처음으로 돌아가기 ; continue
A = 0
while A < 10:
    A = A + 1
    if A % 2 == 0: continue
    print(A)

# 무한 루프
# Ctrl + C 를 눌러서 빠져 나가자

# p125 연습문제 1번 (수기 작성!)
num = 1
result = 0
while num < 100:
    if num % 3 == 0:
        result = result + num
    num = num +1

print(result)

# p125 연습문제 2번 (수기 작성!)
student = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result= 0

while student:
    score = student.pop()
    if score >=50:
        result = result + score

print(result)


# p125 연습문제 3번 (수기 작성!!)
star = '*'
print(star)
print(star * 2)

n = 0
while n < 5:
    n = n +1
    print(star* n)

# 3번 답안
i = 0
while True:
    i += 1
    if i >4 : break
    print('*' * i)

# for문
# 전형적인 for문
testL = ['one', 'two', 'three']
for i in testL:
    print(i)

testL2 = [(1,2), (3,4), (5,6)]
for (first, last) in testL2:
    print(first + last)

# test 결과 
# 1)결과만 출력
score = [90, 25, 67, 45, 80]
for i in score:
    if i >= 60:
        print("good grade!")
    else:
        print("RETAKE")

# 2)학생 번호와 결과 출력
number = 0
for mark in score:
    number = number + 1
    if mark >= 60:
        print("Result : %d student -> pass" % number)
    else:
        print("Result : %d student -> retake" % number) 

# 3)합격만 결과 출력 ; for문에서도 continue 사용 가능
number = 0
for mark in score:
    number += 1
    if mark >= 60:
        print("%d student, congratulations!" % number)
    else:
        continue

# 3)더 간결하게
number = 0
for mark in score:
    number += 1
    if mark < 60:
        continue
    print("%d student, congratulations!" % number)

# for문과 range함수
a = range(1,4)
for i in a:
    print(i)

print(len(a))

# 131p marks3.py
marks = [90, 25,67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60 :
        continue
    print("%d student, pass" % (number +1))

""" ㄴ> marks[number]에는 0~4번의 숫자가 부여되므로, 출력 시에는
        number + 1로 설정
"""

# 구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

"""
    ㄴ> 인수 end를 넣은 이유 : 해당 결과값을 출력할 때
        다음 줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서
    ㄴ> print('')의 의미 : 두번째 for문이 끝나면 결과값을 
        다음 줄부터 출력하게 해준다.
"""

# 리스트 안에 for문 포함 시키기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)

print(result)
