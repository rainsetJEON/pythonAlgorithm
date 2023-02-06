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
# 1번
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)

print(result)

# 2번
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)

print(result)

# 2-1번
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# 3번
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# p134 연습문제 1번
for i in range(1,101):
    print(i)

# p134 연습문제 2번
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
score = 0
avg = 0
for i in A:
    score = score + i

avg = score / len(A)
print(avg)

# p134 연습문제 3번
numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)


# 함수
"""
<함수의 구조>
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
"""

# 함수 예시 1)
def add(a,b):
    return a + b
print(add(3,5))

# 함수 예시 1-2)
def add2(a,b):
    result = a + b
    return result
a = add2(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi!'
a = say()
print(a)

# 결과값이 없는 함수
def plus(a,b):
    print('%d, %d의 합은 %d 입니다.' %(a,b,a+b))
print(plus(3,5))
b = plus(3,4)
print(b)
""" 결과값이 없다는 것의 의미?
    ㄴ> print(b)의 결과가 'None'으로 출력되는 것처럼 
    결과값은 오직 return 명령어로만 돌려받을 수 있다.
"""

# 입력값도 결과값도 없는 함수
def say2():
    print("Hi~")
say2()

# 입력값이 여러 개인 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        
    return result

test1 = add_mul("add", 1,2,3,4,5)
print(test1)
test2 = add_mul("mul", 2,4,5)
print(test2)

# 키워드 파라미너 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = 'Gildong', age=3)
 #ㄴ> 딕셔너리 (key : value)

# 매개변수에 초깃값 미리 설정하기
def myself(name, age, man = True):
    print("My name is %s" % name)
    print("I'm %d years old" % age)
    if man:
        print("man")
    else:
        print("woman")
myself('WJ', 15)
myself('WP', 15, True)
myself('RH',18, False)
# ㄴ> 초깃값을 설정해놓은 변수는 항상 뒤쪽에 위치시켜야 한다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1) return 이용
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

# 2) global 명령어 (비추천)
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)
# ㄴ> global ; 함수 안에서 함수 밖의 a 뱐수를 직접 사용한다. (global 명령어는 독립적으로 존재하는 것이 좋기 때문에 외부 변수에 종속적인 함수에서 사용하기에는 권장하지 않는다.)

# lambda
add = lambda a, b : a+b
result = add(4,7)
print(result)

# p154 연습문제 1번
def is_odd(a):
    if a % 2 == 0 :
        return print("even")
    else:
        return print('odd')

is_odd(4)

# p154 연습문제 2번
def is_normal(*args):
    result = 0
    for i in args:
        sum = result + i
        normal = sum / len(args)
    return normal

A = is_normal(1,2,3,4,5)
print(A)

# 1번 답안
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
is_odd(3)

# 1번 lambda
is_odd2 = lambda a:True if a % 2 == 0 else False
is_odd2(4)

is_odd3 = lambda a:print("even") if a % 2 == 0 else print("odd")
is_odd3(9)

# 04-2 사용자 입력과 출력
for i in range(8):
    print(i, end=' ')

# p157 연습문제 1번
input1 = int(input("first number = "))
input2 = int(input('second number = '))

total = input1 + input2
print(total)

# p158 연습문제 2번 1)
num = input("Enter numbers :")
numbers = num.split(",")
total = 0
for i in numbers:
    total += int(i)
print(total)

# 연습문제 2번 2)
def is_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

A = input("Enter numbers : ")
A = A.split(",")

is_sum(total)

# p158 연습문제 3번
print("you" "need" "python")
print("you" + "need" + "python")
print("you","need","python")
print("".join(["you", "need", "python"]))

# p158 연습문제 4번
