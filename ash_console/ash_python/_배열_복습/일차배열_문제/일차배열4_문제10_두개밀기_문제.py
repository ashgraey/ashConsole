'''
   [문제]
      a 리스트에 있는 값들을 b에 저장하려고 한다. 
      a 리스트의 값을 뒤에서부터 두 개씩 저장하시오.
   [정답]
      b = [7,7,3,3,1,1]
'''

a = [1 ,3, 7]
# a 0 1 2
b = [0, 0, 0, 0, 0, 0]
# b 0 1 2 3 4 5 
'''
b 0 1 =>a 2 
b 2 3 =>a 1 
b 4 5 =>a 0
'''
# [1117]
# aIdx = len(a) - 1 
# bIdx = 0
# for i in range(len(a)) :
#    b[bIdx] = a[aIdx]
#    b[bIdx + 1] = a[aIdx]

#    aIdx -= 1 
#    bIdx += 2
# print(b)
