class TreeNode: #각 노드 [<-,값(벨류),->]
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

#삽입(내부에서 반복 필요X)
def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None: #첫 노드인 경우
        return new_node

    current = root #위치 지정 필요
    while True:
        if value < current.data:        #값이 현재 값보다 작은 경우
            if current.left is None:    #현재 위치에 값이 없으면
                current.left = new_node #현위치에 벨류 삽입
                break
            current = current.left  #좌로 이동
        else:                           #값이 현재 값보다 큰 경우
            if current.right is None:   #현재 위치에 값이 없으면
                current.right = new_node#현위치에 벨류 삽입
                break
            current = current.right  #우로 이동
    return root


#내용 찾기
def search(root, value):
    current = root  #위치 지정
    while True:
        if value == current.data:
            print(f"{value}을(를) 찾았습니다")
            break
        elif value < current.data: #검색값이 현재 값보다 작은 경우
            if current.left is None:
                print(f"{value}이(가) 존재하지 않습니다")
                break
            current = current.left #좌로 이동
        else:
            if current.right is None:#검색값이 현재 값보다 큰 경우
                print(f"{value}이(가) 존재하지 않습니다")
                break
            current = current.right  #우로 이동


#내용 확인(후위순회)
def post_order(node):
    if node is None: #이동 한 노드의 값이 없으면 돌아간다.
        return
    post_order(node.left) #먼저 좌로 이동
    post_order(node.right)#그 다음 우로 이동
    print(f"{node.data} ", end='')#현 노드 출력이 제일 후순위


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers: #반복문으로 삽입
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)

    print()
    find_number = int(input('값 찾기:'))
    search(root, find_number)


    # find_group = int(input())
    #
    # current = root
    # while True:
    #     if find_group == current.data:
    #         print(f"{find_group}을(를) 찾았습니다")
    #         break
    #     elif find_group < current.data:
    #         if current.left is None:
    #             print(f"{find_group}이(가) 존재하지 않습니다")
    #             break
    #         current = current.left
    #     else:
    #         if current.right is None:
    #             print(f"{find_group}이(가) 존재하지 않습니다")
    #             break
    #         current = current.right



