'''
    [정렬]
        [1] 오름차순
        [2] 내림차순
'''
def myUpSort(a):
    for i in range(len(a)):
        j = i
        while j < len(a):
            if a[i] > a[j]: 
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            j += 1

def myReverse(a):
    lastIndex = len(a) - 1
    halfSize = int(len(a) / 2)
    for i in range(halfSize):
        temp = a[lastIndex]
        a[lastIndex] = a[i]
        a[i] = temp
        lastIndex-=1

a = [1001, 3234, 23, 32134, 234]
print(a)

myUpSort(a)
print(a)

myReverse(a)
print(a)

