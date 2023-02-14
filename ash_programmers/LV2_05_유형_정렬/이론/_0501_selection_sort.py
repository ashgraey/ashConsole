# https://heytech.tistory.com/57

def selection_sort(a):
    for i in range(len(a)):
        minIndex = i
        minValue = a[i]
        for j in range(i + 1, len(a)):
            if minValue > a[j]:
                minIndex = j
                minValue = a[j]
            
        a[i], a[minIndex] = a[minIndex], a[i]

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
selection_sort(a)
print('정렬 후:\t', end='')
print(a)