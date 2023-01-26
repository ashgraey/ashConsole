"""
    [딕셔너리키유효성검사]
        딕셔너리에 키값이 존재하는지 찾기
        
"""

item = {"name" : "새우깡" , "price" : 1000}

if "name" in item:
    print(item["name"])
else:
    print("찾는값이 없습니다1.")

print("----------------------------------------------")

if "count" in item:
    print(item["count"])
else:
    print("찾는값이 없습니다2.")