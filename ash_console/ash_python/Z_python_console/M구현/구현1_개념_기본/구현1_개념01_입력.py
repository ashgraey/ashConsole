
"""
    input()  함수
    
    input() 함수는 키보드로 값을 입력하고 엔터를 누를때까지 기다린다. 
    입력한값은 전부 문자열로 저장되며, 숫자를 저장하고싶을땐 형변환해줘야한다.         
"""
print("[test] 당신의 나이를 입력하세요 : " , end=" ")
age = input()
print(age)

# type() 함수 : 데이터의 종류 확인
print(type(age))    # <class 'str'> # 문자열이므로 형변환 해야한다. 

# int() 함수 : 문자 -> 숫자
age = int(age)
print(type(age))    # <class 'int'>


# 방법 1)
print("[1] 당신의 나이를 입력하세요 : " , end="")
age = input()
age = int(age)

# 방법 2)
age = input("[2] 당신의 나이를 입력하세요 : ")
age = int(age)

# 방법 3)
age = int(input("[3]당신의 나이를 입력하세요 : "))
print(age)