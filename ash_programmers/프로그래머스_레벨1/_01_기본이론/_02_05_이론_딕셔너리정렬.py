"""
    [딕셔너리 정렬]
"""

d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

"""
[1] 딕셔너리 key기준 정렬 (오름차순) 
"""
sortedItem = sorted(d.items())
print(sortedItem)

"""
[2] 딕셔너리 key기준 정렬 (내림차순)
"""
sortedItem = sorted(d.items(), reverse=True )
print(sortedItem)

"""
[3] 딕셔너리 value기준 정렬 (오름차순) 
"""
sortedItem = sorted(d.items(), key=lambda x: x[1])
print(sortedItem)

"""
[4] 딕셔너리 value기준 정렬 (오름차순) 
"""
sortedItem = sorted(d.items(), key=lambda x: x[1] , reverse=True)
print(sortedItem)



