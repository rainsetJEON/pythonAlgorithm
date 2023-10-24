# 프로그래머스 스택 예제
# 문제 이름 : 올바른 괄호 ; (,)의 짝 맞는지 확인하기 
def solution(s):
    tmp = []
    for x in s:
        tmp.append(x)
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()

    if len(tmp) == 0:
        return 1
    else:
        return 0
# 이거 뭐더라..? 아닌데 문제 답이..


# 내 답안
def solution(s):
    answer = True
    
    num1 = s.count('(')
    num2 = s.count(')')
    
    if num1 != num2 :
        answer = False
    
    if s[0] == ')':
        answer = False
        
    if s[-1] == '(':
        answer = False
    
    # stack을 쓰자!!!
    # (가 나오면 반드시 )로 닫아줘야 함 -> (이면 cnt +1, )이면 cnt -1
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt +=1
        else:
            cnt -= 1
            if cnt <0:
                answer = False
                break
        

    return answer