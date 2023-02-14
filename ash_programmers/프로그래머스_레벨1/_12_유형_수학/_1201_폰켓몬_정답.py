# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    arr = []
    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
    half = len(nums) / 2
    if half < len(arr):
        return half
    else:
        return len(arr)

nums = [3,1,2,3]
a = solution(nums)
print(a)