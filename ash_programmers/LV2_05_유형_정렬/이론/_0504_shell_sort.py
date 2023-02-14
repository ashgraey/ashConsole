# https://travelbeeee.tistory.com/215

def shell_sort(arr):
    gap = len(arr)
    while True:
        gap = gap // 2
        if gap == 0:
            break
        for i in range(gap , len(a)):
            j = i
            while True:
                if j < gap:
                    break
                if a[j] > a[j - gap]:
                    temp = a[j]
                    a[j] = a[j - gap]
                    a[j- gap] = temp
                j -= gap
    pass



a = [34,65,3,5,8,9,12,2,5,100]
print(a)
shell_sort(a)
print(a)