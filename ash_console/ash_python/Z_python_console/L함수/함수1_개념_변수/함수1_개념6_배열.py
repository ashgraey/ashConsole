'''
    [문제]
        a리스트의 값 중 
        50보다 큰 수만 출력해주는 함수를 만드시오.
    [정답]
        65 76 
'''

def big50(a):
    for i in range(len(a)):
        if a[i] > 50:
            print(a[i], end=" ")

a = [21, 65, 3, 76]
print(a)
big50(a)