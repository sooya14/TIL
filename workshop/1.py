
def start_end(x):
    answer = 0
    for word in x:
        if len(word) >= 2:
            if word[0] == word[-1]:
                answer += 1
            else:
                pass
        else:
            pass
    return answer

keywords = ['level', 'asdwe', 's', 'abadsfa', 'q1q']
print(start_end(keywords))


# a = ['level', 'asdwe', 's', 'abadsfa', 'q1q']

# answer = 0
# for word in a:
#     if len(word) >= 2:
#         if word[0] == word[-1]:
#             answer += 1
#         else:
#             pass
#     else:
#         pass
    
# print(answer)