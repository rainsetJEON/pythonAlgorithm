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

# self의 의미 ; 호출 시 호출한 객체 자신이 전달된다.

# 계산기 만들기
class Fourcal():
    def setdata(self, first, second):   # 메서드의 매개변수
        self.first = first  # 메서드의 수행문
        self.second = second# 메서드의 수행문 

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

"""
 생성자(Constructor)
 ㄴ> 객체가 생성될 때 자동으로 호출되는 메서드
 ㄴ> 파이썬 메서드명으로 __init__을 사용하면 이 메서드는 생성자가 된다.
   ㄴ>__init__메서드는 setdata메서드와 이름만 다르고 동일하지만, 
      생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출
      따라서 호출 시, 바로 data값과 함께 객체를 생성해야 함
      ex) a = FourCal(4,2)
"""

class Fourcal():
    def __init__(self, first, second):
        self.first = first
        self.second = second

#   def setdata(self, first, second):   
#      self.first = first  
#        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

# 클래스의 상속(Inheritance)
# class '새로운 클래스'('기존 클래스')

class More_Cal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

# 메서드 오버라이딩(Overriding, 덮어쓰기)
class SafeFourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return False
        else:
            return self.first / self.second

# 클래스 변수
# 클래스 안에서 선언된 변수로, 클레스에 의해 생성된 모든 객체에 공유된다는 특징을 갖는다.

# p195 연습문제 1번
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(3)
print(cal.value)

# p195 연습문제 2번
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value> 100:
            self.value = 100

cal4 = MaxLimitCalculator()
cal4.add(30)
cal4.add(40)
cal4.add(50)
print(cal4.value)