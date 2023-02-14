# https://seong6496.tistory.com/381

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        print(arr)    
    pass

a = [34,65,3,5,8,9,12,2,5,100]
bubble_sort(a)