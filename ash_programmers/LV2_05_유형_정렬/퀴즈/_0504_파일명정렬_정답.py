# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = []
    arr = []
    for i in range(len(files)):
        head = ""
        number = ""
        tail = ""
        status = "head"
        for j in range(len(files[i])):
            a = files[i][j]
            if status=="head":
                if a not in "0123456789":
                    head += a
                else:
                    status="number"
            if status == "number":
                if a in "0123456789":
                    number += a
                else:
                    status = "tail"
            if status == "tail":
                tail += a
        arr.append([head , number , tail])

    
    #print(arr)
    arr.sort(key=lambda x: (x[0].upper() , int(x[1])))
    #print(arr)

    for i in range(len(arr)):
        answer.append(arr[i][0] + arr[i][1] + arr[i][2])

    return answer


a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#a = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
r = solution(a)
print(r)