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
# [1115]
# aIdx = len(a) - 1 
# count = 0

# for i in range(len(b)) :
#    b[i] = a[aIdx]
#    count += 1 

#    if count % 2 == 0 :
#       i += 1 
#       aIdx -= 1
# print(b)

# [2차]
# b_idx = len(b) - 1
# a_idx = 0 
# for i in range(len(a)) :
#    b[b_idx] = a[a_idx]
#    b[b_idx - 1] = a[a_idx]

#    b_idx -= 2 
#    a_idx += 1
# print(b)
