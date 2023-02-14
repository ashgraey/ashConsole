# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    s1 = str(n)
    s2 = sorted(s1)			# ['a','d','e','f'] 
    s2.reverse()
    s3 = ''.join(s2)		# "adef"
    a = int(s3)
    return a


n = 118372
a = solution(n)
print(a)