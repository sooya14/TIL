# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """
    result = []
    answer = []

    # word 를 하나씩 쪼개서 list 에 넣음 
    for w in word:
        result.append(w)

    # result의 값이랑 index의 전의 자리의 값이 같으면 카운트한다. 
    for i, r in enumerate(result):
        if r == result[i - 1]:
            c = 1
            c += 1
            answer.append(c)

        # 다음 자리의 값이 같지 않으면 r 을 추가  
        else:
            answer.append(r)

    # 만약 숫자가 뒤에 카운트가 안됬을 경우를 완성하지 못했어요 ㅠㅠㅠ  
    # for i, nono in enumerate(result):
    #     if result[i + 1] not in list(range(1, 100):
    #         result[i + 1].append(1)
            
    
    return answer



        

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
