'''
    [리스트 값 삭제 remove함수와 del]
        remove함수와 del을 사용해서 리스트에 값을 삭제할 수 있다.
'''

a = [10, 20, 30, 40]
print("a :", a)

# remove(삭제할 값)를 통해 제거가 가능하다.
a.remove(30)
print("a :", a)

# 아래와 같이 삭제할 수도 있다. (10 삭제)
a.remove(a[0])
print("a :", a)

# del 삭제할 값을 통해 제거가 가능하다.
del a[0]
print("a :", a)