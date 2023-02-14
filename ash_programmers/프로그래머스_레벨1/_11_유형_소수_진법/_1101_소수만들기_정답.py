# https://school.programmers.co.kr/learn/courses/30/lessons/12977

import math

def getPrime(total):
    if total == 2:
        return True
    a = int(math.sqrt(total))
    for i in range(2, a + 1):
        if total % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1 , len(nums)):
                total = nums[i] + nums[j]+ nums[k]
                #print(i , " " , j , " " , k)
                #print(nums[i] , " " , nums[j] , " " , nums[k])
                #print(total)
                #print("---------------------------------------")
                if getPrime(total) :
                    answer += 1
    return answer

nums = 	[1, 2, 7, 6, 4]
result = solution(nums)
print(result)