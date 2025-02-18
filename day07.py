class Node:
    def __init__(self, data, next=None):
        self.data = data    #데이터
        self.next = next    #포인터


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0


    def enqueue(self, data):
        self._size+=1   #사이즈 1증가
        node = Node(data)   #입력 받은 데이터로 노드를 추가

        if self.rear is None: #삽입을 받는 위치가 None 이면
            self.front = node #값을 다음 노드를 저장
            self.rear = node #그 다음 노드로 이동
        else:   #이미 위치가 존재한다면
            self.rear.next =node #노드를 입력
            self.rear = node #그 다음 노드로 이동


    def dequeue(self):
        if self.front is None: #꺼낼 게 없다면
            raise IndexError('dequeue from empty queue')
        self._size -= 1  # 사이즈 1감소
        temp = self.front #백업
        self.front=self.front.next #업데이트
        if self.front is None:
            self.rear = None
        return temp.data


    def size(self) -> int:
        return self._size


if __name__ == "__main__":
    q = Queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    print('size=', q.size())
    print(q.dequeue())
    print('size=',q.size())
