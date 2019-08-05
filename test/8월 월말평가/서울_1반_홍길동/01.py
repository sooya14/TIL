# 파일명 및 함수명을 변경하지 마시오.
def can_divide(numbers, divisor):
    """
    아래에 코드를 작성하시오.
    numbers는 0이 아닌 양의 정수가 담긴 리스트입니다.
    divisor는 0이 아닌 양의 정수입니다.
    numbers에 담겨있는 숫자들 중, divisor로 나누어 떨어지는 숫자들을 오름차순으로 정렬한 리스트를 반환합니다.
    """

    # 방법 1 (정석)
    result = []
    # divisor 로 나눴을 때 나머지가 0이면, result 에 해당 숫자 추가. 
    for number in numbers:
        if number % divisor == 0:
            result.append(number)

    # 모든 numbers 의 요소들을 나눠본 이후, result 가 비었는지 확인. 
    if result == []:
        result.append(-1)

    # 정렬하기
    result.sort()
    return result  # sorted(result)


    # 방법 2 (부가적인 로직)
    # list comprehension ==  나머지가 0인 숫자들 뽑기
    result = [number for number in numbers if not number % divisor]

    return sorted(result) if result else [-1]  
    


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(can_divide([20, 3, 5, 7], 5))
    print(can_divide([4, 3, 2, 1], 1))
    print(can_divide([7, 11, 13], 3))
