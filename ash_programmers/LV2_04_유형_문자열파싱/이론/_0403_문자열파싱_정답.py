
"""
    [1] 아래문자열에서  두글자씩 순서대로 잘라서 리스트에 담아서 출력하시오.
    [2] 공백도 글자에 포함시킨다.
    [3] 단, 두글자전부 알바펫이여야한다. 

        [예시1]
            [1] s = "e=m*c^2  
            [2] [ "e="  , "=m" , "m*" , "*c" , "c^" , "^2" ] 
            [3] 정답 : []
        [예시2]
            [1] s = shake hands
            [2] ["sh" , "ha" , "ak" , "ke" , "e " , " h" , "ha" , "an" , "nd" , "ds"]
            [3] 정답 : ["sh" , "ha" , "ak" , "ke" ,  "ha" , "an" , "nd" , "ds"]

"""

s = "e=m*c^2"
s = "shake hands"
print(s)
arr = []
for i in range(len(s)- 1):
    a = s[i]
    b = s[i + 1]
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if a in sample and b in sample:
        arr.append(a + b)
print(arr)




