
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

# def solution(participant, completion):
    # answer = ''
    #
    # for i in range(len(completion)):
    #     a = completion[i]
    #     if len(participant) != 1:
    #         for j in range(len(participant)):
    #             if a == participant[j]:
    #                 participant.pop(j)
    #                 break
    #
    # answer = participant[0]
    #
    # return answer

def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion):
        if i != j:
            return i


print(solution(participant, completion))