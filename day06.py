# def is_even(n) -> bool:
#     """
#     짝수 판정 함수
#     :param n: 판정할 함수
#     :return: True(짝수면) , False(홀수면)
#     """
#     if n%2==0:
#         return True
#     else:
#         return False
#
# n=int(input("숫자입력: "))
# print(is_even(n))

a=10
b=11
#bit operation(0000 0000)
print(a&b)  #비트 and 연산
print(a|b)  #비트 or 연산
print(a^b)  #비트 서로 다르면 1