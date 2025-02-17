def dec_oct(n) -> int:
    '''
    8진수 변환
    :return: 8진수값
    '''
    if n==0:
        return ""
    else:  #8의 자릿수마다 더해서 계산 (64->100 + (8->10 + (under -> noremal ))
        return dec_oct(n//8) + str(n%8)

n=int(input("8진수로 바꿀 수 :"))
print("==>", dec_oct(n))