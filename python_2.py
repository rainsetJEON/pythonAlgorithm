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

# p125 연습문제 1번
# 벌써 시간이... T^T