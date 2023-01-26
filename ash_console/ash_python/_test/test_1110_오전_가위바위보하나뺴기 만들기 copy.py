'''
가위바위보 하나빼기를 만드시오.

'''
'''
가위0, 바위1, 보2
'''
import random

a1 = random.randint(0,2)
a2 = random.randint(0,2)
b1 = random.randint(0,2)
b2  = random.randint(0,2)

print("가위 바위 보 하나빼기~")
print("a =", a1, a2)
print("b =", b1, b2)

a_ch = random.randint(0,1)
b_ch = random.randint(0,1)
print("a 두개 중 선택 =", a_ch)
print("b 두개 중 선택 =", b_ch)

if a_ch == 0 :
    a_ch = a1
else :
    a_ch = a2

if b_ch == 0 :
    b_ch = b1
else :
    b_ch = b2

print("a가 선택한 값 =", a_ch)
print("b가 선택한 값 =", b_ch)

'''
가위바위보 경우의수
a == b 비김
a       b
if
1바위   0가위 = a가 이김 
2보     1바위 = a가 이김
0가위   2보 = a가 이김

else
0가위   1바위 = b가 이김
1바위   2보   = b가 이김
2보     0가위 = b가 이김
'''
if a_ch == b_ch :
    print("무승부")

elif a_ch == 1 and b_ch == 0 :
    print("a가 이김")  

elif a_ch == 2 and b_ch == 1 :
    print("a가 이김")  

elif a_ch == 0 and b_ch == 2 :
    print("a가 이김")  

else :
    print("b가 이김")

