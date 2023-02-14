# https://jinyes-tistory.tistory.com/30



def insert_sort(arr):
    for i in range(len(arr)):
        last = i
        for j in range(i):
            if arr[last] > arr[last-1]:
                temp = arr[last]
                arr[last] = arr[last-1]
                arr[last-1] = temp
            else:
                break
            last -= 1
        print(arr)
    print(arr)

    pass


a = [34,65,3,5,8,9,12,2,5,100]
insert_sort(a)