'''
   [문제]
      a 리스트에 있는 값들을 b에 저장하려고한다. 
      [조건1] 두개씩 저장한다.
      [조건2] 새로운값이 들어오면 기존의 값들은 한칸씩 뒤로 이동후 저장한다. 
   [예시]
      1 : b = [1,1]
      3 : b = [3,3,1,1]
      7 : b = [7,7,3,3,1,1]
'''
a = [1,3,7]
b = []

# [1115]
# aIdx = len(a) - 1 
# for i in range(len(a)) :
#    b.append(a[aIdx])
#    b.append(a[aIdx])
#    aIdx -= 1 

# print(b)

# [2차]
# # 0으로 이루어진 a의 두배공간의 리스트를 만든다.
# for i in range(len(a) * 2) :
#    b.append(0)
# print(b)

# idx = 0
# bi = len(b) - 1 

# for i in range(len(a)) :
#    b[bi] = a[idx]
#    b[bi - 1] = a[idx]
#    bi -= 2
#    idx += 1 
# print(b)

# [1차]   
# for i in range(len(a)*2):
#    b.append(0)
# print(b)


# index = 0
# # 마지막 인덱스 번호
# bi = len(a) - 1

# for i in range(len(a)):
#    b[index] = a[bi] 
#    # b[0] = a[2]
#    # b[1] = a[1]
#    # b[3] = a[0]
#    index += 1 
#    b[index] = a[bi]
#    #b[1] = a[2]
#    # b[2] = a[1]
#    # b[4] = a[0]
#    index += 1
#    bi -= 1
# print(b)
