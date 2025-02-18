
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:  # if next node exist
            current = current.next  # move
        current.next = Node(data)


    def search(self,target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    #지우기
    def remove(self,target):
        if self.head.data == target: #헤드를 지울 경우
            self.head=self.head.next #헤드를 다음 헤드로
            print('선두노드 삭제')
            return
        current = self.head
        previous = None
        while current:  #중간이 삭제된 경우
            if current.data == target:
                previous.next = current.next
                break #이전 커런트를 기존 커런트의 다음 방향으로 옮김
            else:
                previous = current  #이전 것을 커런트로
                current = current.next  #커런트를 앞의 값으로 옮겨간다.

    #출력 내용
    def __str__(self):
        node = self.head
        while node is not None: #동일 node != None
            print(node.data)#노드 출력
            node=node.next  #다음 노드로
        return "end"


if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    print(l)
    #l.remove(7)
    l.remove(-11)
    print(l)
    l.remove(8)
    print(l)