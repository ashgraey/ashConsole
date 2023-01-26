'''
    [문자열 인덱싱(indexing)]
        문자열도 리스트와 유사하게 인덱싱이 가능하다.
        한글자만 출력하고싶을때는 [] 대괄호와 인덱스 번호로 출력한다. 
'''
text = "python"
print(text[1])

'''
    [문제]
        text변수에서 y만빼고 출력하시오.
'''
for i in range(len(text)):
    if text[i] != 'y':
        print(text[i], end="")
print()
print("--------------------------------")
'''
    [문제]
        text변수에서 가장 마지막글자를 출력하시오.
        마지막글자를 출력하는 모양이 복잡하다.
        text[len(text)-1]
        
        파이썬은 인덱스에 -1 을넣으면 마지막글자를 출력해준다.
        앞부분 len(text) 는 생략할 수 있다.
        text[-1]
        
'''
index = len(text) - 1
print("마지막글자 :", text[index])

print("마지막글자 :", text[-1])