def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        # if char not in table:
        if char in table.values():  # 여는 기호"([{<"
            stack.append(char)  #스텍에 여는 기호 저장
        elif char in table.keys():  # 닫는 기호 ")]}>"
            if not stack or table[char] != stack.pop():
                return False  # 닫는 괄호가 짝이 맞지 앉을 떄
    return len(stack) == 0  # 마지막에 서로 짝이 맞지 않아서 스택에 남은 경우


if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))
