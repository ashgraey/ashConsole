
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
        
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

result = solution(participant , completion)
print(result)