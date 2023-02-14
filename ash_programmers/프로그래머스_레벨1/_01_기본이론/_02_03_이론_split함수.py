"""
[1] split() 함수는 문자열을 구분자로 전부 나눠서 리스트로 만들어준다.
"""
st = "김철수,이만수,김민주"
token = st.split(",")
print(token)

"""
[2] salesData 를 이차원 리스트로 만드시오.
"""
salesData = "새우깡 5,감자깡 6,새우깡 4,콘칩 3,감자깡 7"
tokenList = salesData.split(",")
viewList = []
for i in range(len(tokenList)):
    token = tokenList[i].split(" ")
    viewList.append(token)
print(viewList)

