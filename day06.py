#식 출력
def print_poly(f_x, t_x) -> str:
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]

            # 기호 설정          #맨 앞에는 +를 처리X
        if coefficient >= 0 and i !=0:
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '
    return poly_expression


#x대입해서 계산
def calculation_poly(x_value, f_x, t_x) -> int:
    return_value = 0

    for i in range(len(fx)):
        coefficient = f_x[i]
        term = t_x[i]
        # x앞*(대입 수^차수)
        return_value += coefficient * pow(x_value, term)

    return return_value


fx = [2, 5, -9, 11] #x앞
tx = [20, 7, 2, 0]  #차수

if __name__ == "__main__":
    print(print_poly(fx, tx))
    print(calculation_poly(int(input("x 값 : ")), fx, tx))