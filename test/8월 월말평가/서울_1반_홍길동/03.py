# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """

    # 방법 1 
    count = 1
    seq = 1
    result = [word[0]]
    for seq in range(1, len(word)):
        if word[seq] == word[seq-1]:
            count += 1
                
        else:
            result.append(str(count))
            result.append(word[seq])
            count = 1
    else:
        result.append(str(count))
        return ''.join(result)








# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
