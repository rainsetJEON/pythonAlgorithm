# a = 'I\'m woojin'
# b = 'my name is "woojin".'

# print(b)
# print(a[2])

# 전체 주석 처리 단축키 : ctrl + /

# L1 = "%d apples" %3
# print(L1)
# L2 = ("%d bananas" %4)
# print(L2)

# num = 12
# day = "three"
# L3 = ("%d days, %s babies" %(num, day))
# print(L3)

# percent % 표시하기
# L4 = 'update %-5d%%' %7
# print(L4)

# format 함수
# L5 = "I ate {0} apples, it is {feeling}".format(10, feeling = 'good')
# print(L5)

# 공백 채우기
# L6 = "{0:=^10}".format("hi")
# print(L6)

# L7 = "{0:=<8}".format("hi")
# print(L7)

# join
# ex1 = ".".join('abcd')
# print(ex1)

# ex2 = ".".join(['a', 'b', 'c'])
# print(ex2)

#p63 연습문제 1,2번
# p1 = '881120-1068234'
# birth = p1[0:6]
# id = p1[7:]

# L8 = "gildong birth : %s, id : %s" %(birth, id)
# print(L8)

# p63 연습문제 3번
# d = 'a:b:c'
# d = d.replace(':','#')
# print(d)

# p64 연습문제 4번
# d = 'a:b:c'
# e = d.split(':')
# f = "#".join(e)

# print(d)
# print(e)
# print(f)

# list
'''
list 함수들
삭제 ; del, pop, remove
추가 ; append, insert
 ㄴ>단, insert는 추가하고자 하는 문자의 인덱스를 지정해야 함
정렬 ; sort, reverse
위치반환 ; index
개수 세기 ; count
확장 ; extend
'''
# a = [1, 2, '3', '4']
# print(a[1])
# print(a[2] + a[3])

# a = [1,2,3]
# a[2] = 4
# # print(a)

# del a[0]
# # print(a)

# a.insert(0,5)
# print(a)

# print(a.index(5))

b = [4,5,6]
b.extend([7,8])
print(b)

# p76 연습문제 1번
z = ['life', 'is', 'too', 'short']
z2 = " ".join(z)
print(z2)
print(type(z2))

# tuple 튜플



