# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    
    arr = []
    arr.append(words[0])
    for i , v in enumerate(words):
        if (i + 1) == len(words):
            break
        turn = (i + 1) // n + 1
        people = (i + 1) % n + 1
        a = words[i]
        b = words[i + 1]
       # print(a , b , i , turn , people , end=" , ")

        if a[-1] != b[0]:
            return [people  , turn ]

        if b in arr:
            return [people  , turn ]

        arr.append(b)

        #if people % n == 0:
        #    print()

    return [0,0]
n = 3
words = ["tank", "kick", "know",
 "wheel", "land", "dream",
  "mother", "robot", "tank"]
r = solution(n , words)
print(r)