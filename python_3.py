# 04-3 파일 읽고 쓰기
# p159~

# 5. 클래쓰
class Calculator:
    def __init__(self) :
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.sub(2))

"""
Calculator : 클래스, cal1, cal2 : 객체
클래스를 이용하면 원하는 기능의 독럽적인 객체만 생성해서 사용 가능

*객체와 인스턴스의  차이
(클래스에 의해서 만들어진 객체를 인스턴스라고도 한다.)
a = Calculator() <- a는 객체, a는 클래쓰 Calculator의 인스턴스

*클래스 안에서 구현된 함수는 Method(메서드)라고 부른다.
"""

# 계산기 만들기
class Fourcal():
    def setdata(self, first, second):   # 메서드의 매개변수
        self.first = first  # 메서드의 수행문
        self.second = second# 메서드의 수행문 



