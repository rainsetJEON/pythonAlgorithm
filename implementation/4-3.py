# 4-3 왕실의 나이트


input_data = input()

 # ord('a') = 97
 # chr(97) = a


x = ord(input_data[0])
y = int(input_data[1])


count = 0

steps = [(-1,-2),(+1,-2),(-1,+2),(+1,+2),(-2,-1),(+2,-1), (-2,+1), (+2,+1)]
    
for step in steps:
    nx = x + step[0]
    
    ny = y + step[1]


    if nx >=97 and nx <=103 and ny>=1 and ny <=8:
        count += 1

print(count)
