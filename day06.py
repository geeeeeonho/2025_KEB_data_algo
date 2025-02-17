def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: 판정할 함수
    :return: True(짝수면) , False(홀수면)
    """
    return not n&1

n=int(input("숫자입력: "))
print(is_even(n))