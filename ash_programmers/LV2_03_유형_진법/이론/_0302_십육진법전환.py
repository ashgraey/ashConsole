"""
 [십육진법전환]
    16진법은 0~9 이외에 ABCDEF 를 포함한다. 

    방법은 이진법과 동일하나 나누기 몫이 10~15 일때는 숫자대신 ABCDEF 를 붙여주면된다. 

"""
a = 3456
b = 1
while True:
    if b > a:
        break
    b *= 16
print(a , b) 
st = ''
while True:
    if b == 0:
        break

    c = a // b

    sample = "0123456789ABCDEF"    
    st += sample[c]

    a = a % b
    b = b // 16

print(st)
st = st[1:] # 맨앞의 0을 자른다. 
print(st)