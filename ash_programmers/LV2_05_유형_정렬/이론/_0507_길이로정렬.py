
a = {"aAa" , "bb" , "CCCCC" , "DD" , "ee"}
a = sorted(a , key=lambda x: (len(x) , x.upper()))


for i in range(len(a)):
    print(a[i])

"""
    길이로 정렬 하시오. 길이가 긴순서대로 출력 
    단 , 길이가 같으면 알파벳 낮은순으로 출력 

"""

