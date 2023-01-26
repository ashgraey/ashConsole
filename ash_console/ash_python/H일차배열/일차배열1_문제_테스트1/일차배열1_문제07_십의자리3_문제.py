'''
    [문제]
        a 리스트에서 십의자리가 1이고, 백의자리가 5인 수만 출력하시오.
    [정답]
        510
        512
'''

a = [510,423,124,512,252,23,312,453,122]
size = len(a)

# [1114]
# for i in range(len(a)) :
#     if a[i] % 100 // 10 == 1 and a[i] // 100 == 5 :
#         print(a[i])

# [2차]
# for i in range(size) :
#     if a[i] % 100 // 10 == 1 and a[i] // 100 == 5 : 
#         print(a[i])

# [1차]
# for i in range(size) :
#     if a[i] // 100 == 5:
#         if a[i] % 100 // 10 == 1 :
#             print(a[i])
