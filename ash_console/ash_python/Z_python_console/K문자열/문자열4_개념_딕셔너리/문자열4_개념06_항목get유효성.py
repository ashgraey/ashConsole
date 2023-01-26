"""
    [딕셔너리키유효성검사]
        딕셔너리에 키값이 존재하는지 찾기
        
"""

item = {"name" : "새우깡" , "price" : 1000}

value = item.get("name")
if value == None:
    print("찾는값이 없습니다1.")
else:
    print(value)

print("-----------------------------------------")

value = item.get("count")
if value == None:
    print("찾는값이 없습니다2.")
else:
    print(value)


