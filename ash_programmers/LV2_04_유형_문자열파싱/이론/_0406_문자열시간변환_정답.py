
arr = ["12:04,13:00" , "21:47,23:45"]

brr = []
"""
위 arr 배열은 시간을 표현한것이다. 
12:04분이 시작이고 13:00 이 마감이라고 했을때, 
각각의 시간차를 brr배열에 저장하시오. 

brr = [60, 120]
"""


for i in range(len(arr)):
    temp = arr[i]
    token = temp.split(",")
    print(token)
    token2 = token[0].split(":")
    a = int(token2[0])
    b = int(token2[1])

    token3 = token[1].split(":")
    c = int(token3[0])
    d = int(token3[1])

    total1 = a * 60 + b
    total2 = c * 60 + b
   
    brr.append(total2-total1)
print(brr)
