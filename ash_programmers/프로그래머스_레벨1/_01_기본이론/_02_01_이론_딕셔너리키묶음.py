"""
[1] 딕셔너리 키묶음찾기
    딕셔너리는 keys() 함수를 이용해서 key값들을 모두 찾은후, key로 value를 찾을수있다. 
"""
di = {"a" : 0 , "b" : 1 , "c" : 2}
print(di.keys())
print("------------------------")
"""
[1] 딕셔너리 출력
    for 문을 활용해서 아래와 같이 출력할수있다.
"""
for key in di.keys():
    print(key , " " , di[key])
