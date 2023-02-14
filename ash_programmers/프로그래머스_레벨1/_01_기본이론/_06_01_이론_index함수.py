"""
    index() 함수를 이용해서 리스안의 값을 찾을수있다.
    단, 값이 없으면 에러가 발생되기 때문에 반드시 in 키워드로 존재여부를 확인후에 해야하낟.
"""

a = [10,20,30,40,50]
idx = a.index(20)
print(idx) # 1 잘나온다.

# idx2 = a.index(70) # 에러가 발생한다. 
# 아래와 같이 in 키워드로 검사후레 index() 함수를 사용한다. 
if 70 in a:
    idx2 = a.index(70)
    print(idx2)
else:
    print("찾는값이 없다.")