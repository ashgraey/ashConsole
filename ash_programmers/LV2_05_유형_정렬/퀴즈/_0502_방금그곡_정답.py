# https://school.programmers.co.kr/learn/courses/30/lessons/17683

class Node:
    startTime = 0
    endTime = 0
    totalTime = 0
    sub = []
    music = []

    def printAll(self):
        print(self.startTime , self.endTime , self.totalTime , self.sub , self.music)

def getTime(startTime, endTime):
    if startTime == endTime:
        return 0
    tok1 = startTime.split(":")
    tok2 = endTime.split(":")
    total1 = int(tok1[0]) * 60
    total1 += int(tok1[1])
    total2 = int(tok2[0]) * 60
    total2 += int(tok2[1])
    if endTime == "00:00":
        total2 = 24 * 60
    return total2 - total1 
    pass


def getMusic(st):

    sample1 = ["A#" , "B#" , "C#" , "D#" , "E#" , "F#" , "G#"]
    sample2 = ["a" , "b" , "c" , "d" , "e" , "f" , "g"]

    for i in range(len(sample1)):
        if sample1[i] in st:
            st = st.replace(sample1[i] , sample2[i] )
    return st
def solution(m, music):
    
    temp = 0
    lastArr = []
    nodeList = []
    for i in range(len(music)):
        token = music[i].split(",")
        node = Node()
        node.startTime = token[0]
        node.endTime = token[1]
        node.totalTime = getTime(token[0] , token[1])
        node.sub = token[2]
        node.music = getMusic(token[3])
        tempMusic = getMusic(m)
        if len(node.music) < node.totalTime:
            while len(node.music) < node.totalTime:
                node.music *= 2     
        node.music = node.music[:node.totalTime]
        if tempMusic in node.music:
            nodeList.append(node)
    
    if len(nodeList) > 0:
        nodeList.sort(key=lambda x: (-x.totalTime))
        return nodeList[0].sub
    return "(None)"

m , music = "ABC" , ["12:04,13:00,HELLO,ABC#ABC#ABC"]
m , music = "CC#BCC#BCC#BCC#B" , ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
r = solution(m , music)
print(r)


