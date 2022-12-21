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


