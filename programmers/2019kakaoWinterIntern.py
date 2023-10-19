def solution(s):
    
    answer = []
    string = s.replace('{', '')
    string = string.replace('}', '')
    
    count = dict()
    
    string = string.split(',')
    
    for x in string:
        x= int(x)
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
            
    print(count)
    
    answer = sorted(count, key = lambda x:count[x], reverse = True)
    
    
    
    return answer