# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """

    # 방법 1 
    result = []
    tmp = []  # 임시적으로 거쳐갈 리스트 

    for char in word:
        # tmp 가 비어있지 않고, 
        # tmp 의 마지막 글자가 지금 char 와 같지 않다면
        if tmp and tmp[-1] != char:
            result.append(tmp[-1]) 

        tmp.append(char)








# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
