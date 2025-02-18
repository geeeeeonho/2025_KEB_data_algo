class Stack:
    def __init__(self): #스택 생성
        self.items=[]

    def push(self , data):  #실질 삽입
        self.items.append(data)

    def pop(self):  #팝(리턴 후 삭제)
        return self.items.pop()

    def size(self): #스택 안의 아이템 크기 재기
        return len(self.items)

    def peek(self): #픽(이전 거를 보기)
        return self.items[-1]

s1=Stack()
s1.push(-9)
s1.push(11)
s1.push(-977)
print(s1.pop())
print(s1.peek())