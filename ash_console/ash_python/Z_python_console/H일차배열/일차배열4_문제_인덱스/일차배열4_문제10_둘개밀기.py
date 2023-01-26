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
for i in range(len(a)*2):
   b.append(0)
index = 0
bi = len(a) - 1
for i in range(len(a)):
   b[index] = a[bi]
   index += 1
   b[index] = a[bi]
   index += 1
   bi -= 1
print(b)